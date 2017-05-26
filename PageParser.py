import urllib.request
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from html.parser import HTMLParser


#The dictionary below contains all of the html tags and their associated data
#in the following (key : pair) format. (pageIndex : data) 
#Currently this dictionary does not contain the Attributes of the tags
htmlPage = {}

#Ditionary containing (pageIndex : hyperlink)
links = {}

porter = PorterStemmer()

stopWordList = stopwords.words('english')

def trimSentence(text):
    clean = []
    sent = re.sub(r'[^\x00-\x7F]', '', text)
    for w in re.split('\s', sent): # TODO: from nltk.tokenize import word_tokenize
        word = str(re.sub(r'\W+', '', w)).lower()
        if word not in stopWordList:
            clean.append(porter.stem(word))
    return clean

class MyHTMLParser(HTMLParser):

    #This is the global index for htmlPage and links
    pageIndex = 0

    def handle_starttag(self, tag, attrs):
        #increment the page index for every tag seen 
        self.pageIndex += 1
        for a in attrs:
            if re.search(r'href', a[0]):
                links[self.pageIndex] = a

    def handle_data(self, data):
        #check if there are words in the data and there is an index
        if re.search(r'\w+', data) and self.pageIndex:
            htmlPage[self.pageIndex] = trimSentence(data)
            #print(trimSentence(data))

    def handle_comment(self, data):
        #comments are assumed useless
        #however if the comments are not caught by the parser they are interpreted as data
        pass

parser = MyHTMLParser()
with urllib.request.urlopen('https://academic.oup.com/nar/article/38/suppl_2/W214/1126704/The-GeneMANIA-prediction-server-biological-network#20150589') as f:
    parser.feed(f.read().decode('utf-8'))

for i in htmlPage.keys():
    print(htmlPage[i])     