from nltk.tokenize import sent_tokenize, word_tokenize
from topics import *

# TODO: create class that includes both the text and the links as lists and put this into all following functions

def get_info(parser):
    site = textLinks(parser)
    sectioned = section_text(site[0], site[1:])
    return clean(sectioned)

# gets all of the useful text and has links that point to the places in the text which they are associated with
def textLinks(parser):
    text='TODO'
    links=[]
    return text, links

# split into sentences or paragraphs or places inbetween text
def section_text(text, links):
    text = text.split()
    return text

def clean(text): # TODO: Get synonyms with synset
    cleaned = []
    sent = re.sub(r'[^\x00-\x7F]', '', text)
    for w in text: # TODO: from nltk.tokenize import word_tokenize
        word = str(re.sub(r'\W+', '', w)).lower()
        if word not in stopWordList:
            cleaned.append(porter.stem(word))
    return cleaned