from html.parser import HTMLParser
from topics import *

class MyHTMLParser(HTMLParser):
    #The dictionary below contains all of the html tags and their associated data
    #in the following (key : pair) format. (pageIndex : data) 
    #Currently this dictionary does not contain the Attributes of the tags
    htmlPage = {}

    #Ditionary containing (pageIndex : hyperlink)
    links = {}


    #This is the global index for htmlPage and links
    pageIndex = 0

    def handle_starttag(self, tag, attrs):
        #increment the page index for every tag seen 
        self.pageIndex += 1
        for a in attrs:
            if re.search(r'href', a[0]): # TODO: the numerical links are not href's
                self.links[self.pageIndex] = a # TODO: link is associated with the text after, not before

    def handle_data(self, data):
        #check if there are words in the data and there is an index
        if re.search(r'\w+', data) and self.pageIndex:
            self.htmlPage[self.pageIndex] = trimSentence(data)
            #print(trimSentence(data))

    def handle_comment(self, data):
        #comments are assumed useless
        #however if the comments are not caught by the parser they are interpreted as data
        pass

