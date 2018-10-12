import unittest
from deepcite import main
from deepcite import Utils

def baseTest():
    start_site='http://www.aauw.org/research/the-simple-truth-about-the-gender-pay-gap/'
    start_text='As a result, women who complete college degree are less able to pay off their student loans promptly, leaving them paying more and for a longer time than men.'
    iteration = 0
    return main.be_all_end_all(Utils.node(start_text, start_site), iteration)

def test_base():
    assert baseTest() != ""

baseTest()