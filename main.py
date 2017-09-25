#import PageParser as pp
from TextParser import *
from utils import *
from visualize import visualize
import urllib.request

max_it = 5

def be_all_end_all(node, iteration):
    iteration+=1
    parser = Parser(node.site)
    page = get_info(parser)
    children = find_closest(node.text, page)
    visualize(children)
    if(iteration<max_it):
        for child in children:
            be_all_end_all(child, iteration+1)

if __name__ == '__main__':
    start_site='http://www.aauw.org/research/the-simple-truth-about-the-gender-pay-gap/'
    start_text='As a result, women who complete college degree are less able to pay off their student loans promptly, leaving them paying more and for a longer time than men.'
    #parser = pp.Parser(start_site)

    iteration = 0
    be_all_end_all(node(start_text, start_site), iteration)