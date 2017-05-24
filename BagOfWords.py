import re 
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

porter = PorterStemmer()
stopWordList = stopwords.words('english')

def trimSentence(text):
	clean = []
	sent = re.sub(r'[^\x00-\x7F]', '', text)
	for w in re.split('\s', sent):
		word = str(re.sub(r'\W+', '', w)).lower()
		if word not in stopWordList:
			#clean.append(porter.stem(word))
			clean.append(word)
	return ' '.join(clean)