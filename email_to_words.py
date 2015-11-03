from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk.corpus import wordnet 
import re

p_stemmer = SnowballStemmer("english")

def email_to_words(email_body, stem=False, english=False):
    # Function to convert a raw email to a string of words
    # The input is a single string (a email ), and 
    # the output is a single string (a preprocessed email
    #
    # Remove instances of \n
    email_text=re.sub("\n"," ", email_body)
    #
    # Remove instances of B6
    email_text=re.sub("B6","", email_text)
    #
    # Replace instances of "pis" with "pls"
    email_text=re.sub(r"pis|Pis","please",email_text)
    # Remove email addresses
    email_text=re.sub(r"[\w]+@[\.\w]+","",email_text)
    #
    # Remove web addresses
    email_text=re.sub(r"(https\://|hop\://|ttp\://|www?\.)\S+","",email_text) 
    #
    # Remove boilerplate U.S. State Department 
    email_text=email_text.split(r"U\.S\. Department of State",1)[0]
    #
    # Remove boilerplate mobile signature
    email_text=re.sub(r"(Sent from my)(iPad|Verizon Wirless 4G LTE DROID|HTC Touch Pro|Verizon Wireless Blackberry|Blackberry Wireless Handheld|iPhone|mobile device)","",email_text)
    #
    # Remove non-letters        
    letters_only = re.sub("[^a-zA-Z]", " ", email_text) 
    #
    # Convert to lower case, split into individual words
    words = letters_only.lower().split()
    #
    # Remove month and day of week
    monthday=["january", "february","march","april","may","june","july","august"\
             ,"september","october","november","december","monday","tuesday"\
             ,"wednesday","thursday","friday","saturday","sunday"]
    #         
    words=[w for w in words if not w in monthday]
    # In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))                  
    #
    # Remove stop words
    meaningful_words = [w for w in words if not w in stops]   
    #
    # Remove words less than two characters
    meaningful_words=[w for w in meaningful_words if len(w)>2]
    #
    if stem==True:
        # Stem words
        meaningful_words = [p_stemmer.stem(i) for i in meaningful_words]
    if english==True:
        #Remove non-english words
        meaningful_words=[w for w in meaningful_words if wordnet.synsets(w)]
    #
    # Join the words back into one string separated by space, 
    # and return the result.
    return( " ".join( meaningful_words ))
    #return email_text
