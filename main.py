import PageParser as pp
from TextParser import *
from topics import *
import urllib.request


def be_all_end_all(text, site):
    parser = pp.MyHTMLParser()
    with urllib.request.urlopen(site) as f:
        parser.feed(f.read().decode('utf-8'))

    page = get_info(parser)
    children = find_closest(text, page)
    visualize(children)
    if(iteration<max_it):
        for child in children:
            be_all_end_all(child)

if __name__ == '__main__':
    parser = pp.MyHTMLParser()
    with urllib.request.urlopen('https://academic.oup.com/nar/article/38/suppl_2/W214/1126704/The-GeneMANIA-prediction-server-biological-network#20150589') as f:
        parser.feed(f.read().decode('utf-8'))

    text = "The two non-adaptive methods are the most conservative options and work well on small gene lists"
    start_site=''
    start_text=''
    be_all_end_all(start_text,start_site)