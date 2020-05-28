import pandas as pd
import glob
import process_documents_2 as p
import re


## A Mapping from unique integer document IDs to a bag of words:

def return_bag_of_words(files_list):
	dataframe = [[]]
	doc_id = 0
	for file in files_list:
		print("Processing Document ",doc_id," for Bag of Words...")
		row = []

		doc_id = doc_id + 1
		row.append(doc_id)

		if re.match('.*business.*',file):
			row.append('b')
		elif re.match('.*entertainment.*',file):
			row.append('e')
		elif re.match('.*politics.*',file):
			row.append('p')
		elif re.match('.*sports.*',file):
			row.append('s')
		elif re.match('.*tech.*',file):
			row.append('t')
		else:
			row.append('default_label')	

		f = open(file,"r")
		content = f.read()

		bag_of_words = p.process_document(content)
		bag_of_words = list(set(bag_of_words))
		#print(bag_of_words)
		row.append(bag_of_words)

		dataframe.append(row)

	return dataframe

## A mapping from words to number of documents it appears in, NOT the total number of times it 
## appears across all documents

def return_document_word_count(word_doc_dictionary):

	print("Processing words for their counts in unique Documents...")

	word_doc_count = [['word','doc_count']]
	first = 1
	for row in word_doc_dictionary:
		if first == 1:
			first = 2
		else:
			word_doc_count.append([row[0],len(row[2])])

	return word_doc_count



## word ids: a mapping from words to unique IDs

def word_docid_list(df):

	print("Processing words to find their occurances in every document...")
	word_id = 1
	r = [['word','word_id','doc_list']]
	words_list = []
	for row in df:
		if row != []:
			words_list = words_list + row[2]

	words_list = list(set(words_list))


	for word in words_list:
		doc_list = []
		for row in df:
			if row != []:
				if word in row[2]:
					if doc_list != []:
						doc_list = doc_list + "," + str(row[0])
					else:
						doc_list = str(row[0])

		dict_words = [word, word_id, doc_list]
		r.append(dict_words)
		word_id = word_id + 1


	return r







	## labels: a mapping from unique document IDs to labels
	## ( one of 'e','p','t','s'or 'b' for entertainment, politics, technology, sports, business respoctively)
	## You can get this lable from the filename variable. 
	## Each file is names using Following Schema:
	## L_XXX.txt where L is a one character label and XXX is a three digit ID. 
	## Do_NOT use these IDs when calculating documents though, since these IDs are not guaranteed to be unique across the different labels
	## (i.e. We can have both a b_001.txt and s_001.txt) 



txtfiles = []

for file in glob.glob("C:\\Users\\HP\\Documents\\bbc-fulltext\\bbc\\business\\*.txt"):
	txtfiles.append(file)
for file in glob.glob("C:\\Users\\HP\\Documents\\bbc-fulltext\\bbc\\entertainment\\*.txt"):
	txtfiles.append(file)
for file in glob.glob("C:\\Users\\HP\\Documents\\bbc-fulltext\\bbc\\politics\\*.txt"):
	txtfiles.append(file)
for file in glob.glob("C:\\Users\\HP\\Documents\\bbc-fulltext\\bbc\\sports\\*.txt"):
	txtfiles.append(file)
for file in glob.glob("C:\\Users\\HP\\Documents\\bbc-fulltext\\bbc\\tech\\*.txt"):
	txtfiles.append(file)

dataframe_1 = return_bag_of_words(txtfiles)
df_1 = pd.DataFrame(dataframe_1)
df_1.columns = ["doc_id","label","bag_of_words"]
df_1 = df_1.dropna()
df_1.to_csv("doc_to_bag_of_words.csv", index=False, header=True)

words_dictionary = word_docid_list(dataframe_1)
df_2 = pd.DataFrame(words_dictionary)
#print(df_2)
df_2.to_csv("words_in_docList.csv", index=False, header=False)

word_doc_count = return_document_word_count(words_dictionary)
df_3 = pd.DataFrame(word_doc_count)
#print(word_doc_count)
df_3.to_csv("word_in_docs_Count.csv", index=False, header=False)





