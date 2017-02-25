import urllib.request
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_startendtag(self, tag, attrs):
        print("Start Tag : ", tag)
        for a in attrs:
            try:
                print(" Attr : ", a)
            except UnicodeEncodeError:
                print(" attr    ")

    def handle_endtag(self, tag):
        print("End Tag : ", tag)

    def handle_data(self, data):
        try:
            print("Data : ", data)
        except UnicodeEncodeError:
            print(" data    ")

parser = MyHTMLParser()
with urllib.request.urlopen('https://academic.oup.com/nar/article/38/suppl_2/W214/1126704/The-GeneMANIA-prediction-server-biological-network#20150589') as f:
    parser.feed(f.read().decode('utf-8'))