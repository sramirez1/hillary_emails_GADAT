import pickle
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
import nltk
import re

p_stemmer = SnowballStemmer("english")

clean_emails = pickle.load( open( "output/clean_emails.p", "rb" ) )
def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [p_stemmer.stem(t) for t in filtered_tokens]
    return stems

from gensim import corpora, models, similarities 
#tokenize
token_emails = [tokenize_and_stem(text) for text in clean_emails]

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(token_emails)

#remove extremes
dictionary.filter_extremes(no_below=1, no_above=0.8)

dictionary.compactify()

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in token_emails]
final=models.ldamodel.LdaModel.load('output/final_topic10.model')
import pyLDAvis.gensim as gensimvis
import pyLDAvis
vis_data = gensimvis.prepare(final, corpus, dictionary)
pyLDAvis.display(vis_data)