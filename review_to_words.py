
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import nltk
from bs4 import BeautifulSoup
import re
from nltk.stem.snowball import SnowballStemmer

p_stemmer = SnowballStemmer("english")

def review_to_words(email_body):
    # Function to convert a raw review to a string of words
    # The input is a single string (a raw movie review), and 
    # the output is a single string (a preprocessed movie review)
    #
    # 1. Remove HTML
    email_text = BeautifulSoup(email_body).get_text() 
    #
    # Remove instances of \n
    email_text=re.sub("\n"," ", email_text)
    # Remove boilerplate U.S. State Department 
    email_text=email_text.split("U.S. Department of State",1)[0]
    # 2. Remove non-letters        
    letters_only = re.sub("[^a-zA-Z]", " ", email_text) 
    #
    # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split()
    
    # 4. Remove "\n" line endings
    #line_endings=re.sub("\n"," ", words)
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))                  
    #
    # 5. Remove stop words
    meaningful_words = [w for w in words if not w in stops]   
    #
    # Stem words
    stemmed_tokens = [p_stemmer.stem(i) for i in meaningful_words]

    # 6. Join the words back into one string separated by space, 
    # and return the result.
    return( " ".join( stemmed_tokens ))
    #return email_text