from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer 
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
import re

def process_document(file):
	# consistent casing
	file = file.lower()

	# Tokenization
	file = re.sub('[^A-Za-z0-9\s]+', '', file)
	words = word_tokenize(file)
	#return words

	# Removing Common words - stop words
	clean_list = []
	stop_words = stopwords.words('english')
	stop_words.append(["etc", "also"])
	for word in words:
		if word not in stop_words:
			clean_list.append(word)


	# Stemming - Using this one - the below ones are just for reference:
	lemmatizer = WordNetLemmatizer()
	stemmer = PorterStemmer()
	words = []
	for word in clean_list:
		w = lemmatizer.lemmatize(word,pos='a')
		if w == word:
		 	w = lemmatizer.lemmatize(w,pos='v')
		if w == word:
		 	w = lemmatizer.lemmatize(w,pos='n')
		if (w == word) and (len(w)) > 3:
		 	w = stemmer.stem(w)
		words.append(w)

	return words

