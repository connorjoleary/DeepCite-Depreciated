import re 
#import stopwords
from nltk.corpus import stopwords
stopWordList = stopwords.words('english')

def trimData(data):
	dataList = re.split('\s', data)
	print(dataList)