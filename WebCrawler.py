import urllib.request
import re
from html.parser import HTMLParser

#The dictionary below contains all of the html tags and their associated data
#in the following (key : pair) format. (pageIndex : data) 
#Currently this dictionary does not contain the Attributes of the tags
htmlPage = dict()

#Ditionary containing (pageIndex : hyperlink)
links = dict()

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
        #check if there are tags and valid data to add
        if re.search(r'\w+', data) and self.pageIndex:
            htmlPage[self.pageIndex] = data

    def handle_comment(self, data):
        #similarly this adds comments to the dictionary
        if data and self.pageIndex:
            htmlPage[self.pageIndex] = data

parser = MyHTMLParser()
with urllib.request.urlopen('https://academic.oup.com/nar/article/38/suppl_2/W214/1126704/The-GeneMANIA-prediction-server-biological-network#20150589') as f:
    parser.feed(f.read().decode('utf-8'))

#prints out the link item associated with a htmlPage data
for h, v in htmlPage.items():
    for l, d in links.items():
        if h == l:
            try:
                print(v, d)
            except UnicodeEncodeError:
                print(h, l)