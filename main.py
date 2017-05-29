import PageParser as pp
from topics import *
import urllib.request

if __name__ == '__main__':
    parser = pp.MyHTMLParser()
    with urllib.request.urlopen('https://academic.oup.com/nar/article/38/suppl_2/W214/1126704/The-GeneMANIA-prediction-server-biological-network#20150589') as f:
        parser.feed(f.read().decode('utf-8'))

    text = "The two non-adaptive methods are the most conservative options and work well on small gene lists"
    most=0.0
    for i in parser.htmlPage.keys():
        dist = cosign_dist(trimSentence(text),parser.htmlPage[i])
        if not dist==0.0:
            # print(htmlPage[i])
            # print(dist)
            if dist > most:
                most = dist
                print(parser.htmlPage[i])
                print(dist)
                print(parser.links.get(i))