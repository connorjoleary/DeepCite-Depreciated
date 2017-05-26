from nltk.tokenize import sent_tokenize, word_tokenize
import PageParser as pp

def get_vector(text):
    words = pp.trimSentence(text)

def find_closest(cite, page):
    vec = get_vector(cite)
    