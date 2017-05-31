import PageParser as pp
from topics import *
import urllib.request

if __name__ == '__main__':
    parser = pp.MyHTMLParser()
    with urllib.request.urlopen('https://academic.oup.com/nar/article/38/suppl_2/W214/1126704/The-GeneMANIA-prediction-server-biological-network#20150589') as f:
        parser.feed(f.read().decode('utf-8'))

    text = "The two non-adaptive methods are the most conservative options and work well on small gene lists"
    find_closest(text, parser)