import re 
#import stopwords
#from nltk.corpus import stopwords
#stopWordList = stopwords.words('english')
stopWordList = ["a", "about," "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few",
"for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me",
"more", "most", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll",
"they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's" "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself",'yourselves']


def trimData(data):
	dataList = []
	for x in re.split('\s', data):
		word = str(x).lower()
		if word not in stopWordList:
			dataList.append(word)
	print(dataList)

class BagOfWords():

	def __init__(self):
		self.wordTable = {}

	def addWord(self, word):
		if word in self.wordTable.keys():
			self.wordTable[word] += 1
		else:
			self.wordTable[word] = 1

	def addSentence(self, sentence):
		for w in re.split('\s', sentence):
			word = str(re.sub(r'\W+', '', w)).lower()
			#word = str(w).lower()
			if word in self.wordTable.keys():
				self.wordTable[word] += 1
			else:
				self.wordTable[word] = 1