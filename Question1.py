import re
import string
import os
import sys
import numpy as np

def function(s):
    return re.sub("[%s]" % re.escape(string.punctuation), '', s.lower())


def main():	
	
	if len(sys.argv) > 1:
		inFile = sys.argv[1]
	else:
		inFile = 'Test.txt'
	
	print(inFile)
	words=[]
	sentenceList=[]
	no_sentences=0
	
	with open(inFile,'r') as f:
		 #Loop through file line by line
		for line in f:
			#input words into list
			words.extend(line.split())
			#Count # of sentences - End of sentences are: . ! ? and may be followed by  " 
			no_sentences+=len(re.findall(r' *[\.\?!][\'"\)\]]* *', line))
			sentenceEnders = re.compile(r' *[\.\?!][\'"\)\]]* *')
			sentenceList += sentenceEnders.split(line) 
				   
	
	#Get Unique words form word list        
	unique_words = set(words)

	#Get average # words per sentence
	wordcounts=[] # per sentence
	for sentence in sentenceList:
		words2 = sentence.split(' ')
		wordcounts.append(len(words2))
	average_wordcount = sum(wordcounts)/len(wordcounts)

	#Frequency of words
	wordfreq = []
	for w in words:
		wordfreq.append(words.count(w))
	WordFreq=np.column_stack((words, wordfreq))
		
	#Print Results    
	print('Total word count: '+ str(len(words)))
	print('Unique words: '+ str(len(unique_words)))
	print('Sentences: '+ str(no_sentences))
	print('Avg. Word Count: '+ str(average_wordcount))
	print('Words Used and their Frequency:')
	print(np.sort(WordFreq))

if __name__ == "__main__":	
	main()

