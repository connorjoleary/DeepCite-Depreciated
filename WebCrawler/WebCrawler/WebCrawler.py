import urllib.request
import re
from html.parser import HTMLParser

#The dictionary below contains all of the html tags and their associated data
#in the following (key : pair) format. ((tag name, occurance number) : data) 
#Currently this dictionary does not contain the Attributes of the tags
htmlPage = dict()

#This is a list of tuples (tag, occurance), which are the keys of htmlPage
tagList = list()

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        #add tuple key to list, use len(tagList) + 1 to avoid NoneType error 
        tagList.append((tag,len(tagList)+1))

    def handle_data(self, data):
        #check if there are tags and valid data to add
        try:
            if re.search(r'\w+', data):
                print(data)
        except UnicodeEncodeError:
            print("*************")

    def handle_comment(self, data):
        #similarly this adds comments to the dictionary
        if data and tagList:
            commentKey = ("Comment", tagList[-1][1])
            htmlPage[commentKey] = data

parser = MyHTMLParser()
with urllib.request.urlopen('https://academic.oup.com/nar/article/38/suppl_2/W214/1126704/The-GeneMANIA-prediction-server-biological-network#20150589') as f:
    parser.feed(f.read().decode('utf-8'))