from nltk.tokenize import sent_tokenize, word_tokenize
#import PageParser as pp
import re,math
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import Counter

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

def find_closest(cite, page):
    print("TODO")

def trimSentence(text):
    clean = []
    sent = re.sub(r'[^\x00-\x7F]', '', text)
    for w in re.split('\s', sent): # TODO: from nltk.tokenize import word_tokenize
        word = str(re.sub(r'\W+', '', w)).lower()
        if word not in stopWordList:
            clean.append(porter.stem(word))
    return clean
