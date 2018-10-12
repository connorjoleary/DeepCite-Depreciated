#import PageParser as pp
import urllib.request

from .Compair import *
from .TextParser import Parser, get_info
from .Utils import *
from .Visualize import visualize

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
