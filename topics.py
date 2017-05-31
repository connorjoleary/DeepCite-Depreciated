from nltk.tokenize import sent_tokenize, word_tokenize
#import PageParser as pp
import re,math
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import Counter


class node():
    def __init__(self, text, site):
        self.text = text
        self.cite = site

porter = PorterStemmer()
stopWordList = stopwords.words('english')

def get_vector(text):
    return Counter(text)

def cosign_dist(text1,text2):
    vec1=get_vector(text1)
    vec2=get_vector(text2)

    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

# returns the closest sections of text and their respective links, 
# TODO: draw a social network map
def find_closest(cite, page): # TODO: if nothing good is returned by going sentence by sentence then broaden the search

    most=0.0
    most_i = -1
    for i in parser.htmlPage.keys():
        dist = cosign_dist(trimSentence(text),parser.htmlPage[i])
        if not dist==0.0:
            # print(htmlPage[i])
            # print(dist)
            if dist > most:
                most = dist
                most_i=i
                print(parser.htmlPage[i])
                print(dist)
                print(parser.links.get(i))
    return node(parser.htmlPage[most_i], parser.links.get(most_i))