#import PageParser as pp
from TextParser import *
from utils import *
from Compair import *
from visualize import visualize
import urllib.request

max_it = 5
start_text=''

def be_all_end_all(node, iteration):
    parser = Parser(node.site)
    source = prepare_source(start_text)
    page = get_info(parser)
    children = find_closest(source, page, compute_smallest_distance())
    if(iteration<max_it and children != None):
        for child in children:
            visualize(children)
            be_all_end_all(child,  iteration+1)
    else: #TODO: need a better ending
        if (children == None):
            return [node]
        else: 
            return children