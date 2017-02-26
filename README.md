# DataChallenge

I completed a data challenge for Flock with a 2 hr limit, in this repository you will find my files for this challenge. In this post I will walk you through the challenge.

___
## Question 1 

Create a text content analyzer. This is a tool used by writers to find statistics such as word and sentence count on essays or articles they are writing.

Write a Python program that analyzes input from a file and compiles statistics on it. The program should output:
- The total word count.
- The count of unique words.
- The number of sentences.

Example output:

Total word count: 468
Unique words: 223
Sentences: 38

Brownie points will be awarded for the following extras:
The ability to calculate the average sentence length in words.
The ability to find often used phrases (a phrase of 3 or more words used over 3 times).
A list of words used, in order of descending frequency.
The ability to accept input from STDIN, or from a file specified on the command line.

This question should be written in Python. 

___
My code for this question is found in [here](https://github.com/adrifloresm/DataChallenge/blob/Draft/Question1.py).

First to get the total word count and number of unique words: I open the input file and as I loop through the file line by line. As I loop through the lines I split the words and add them to a word list.

```python
with open(inFile,'r') as f:
		 #Loop through file line by line
		for line in f:
			#input words into list
			words.extend(line.split())
```
After generating a list with *all* the words in the document, we can get the unique words of the list by using the command [set](https://docs.python.org/2/library/sets.html) - unordered collection of unique elements.
```python
#Get Unique words form word list        
	unique_words = set(words)
  ```
 After these we are ready to print the first set of results *Total word count* and *Number of Unique words*. To get the number of these values, we need to get the length of our lists `words` and `unique_words`, also to display these values we must convert them to strings to be added to the print command.
 
 ```python
 #Print Results    
	print('Total word count: '+ str(len(words)))
	print('Unique words: '+ str(len(unique_words)))
  ```
  
  The next step in this question is to get the number of sentences. There is multiple ways to do this, however we can take advantage that we are already looping through the file line by line to help us find the number of sentences. The way we do this is to find the end of a sentence and count how many times that happens in the line. And as we loop through the lines of the file we add the number of sentences per line to a counter.
  
 There are several key components to note when determining the end of a sentence. A sentence can end in more than just a period (.) , it may also end in ! or ? , as well as ".  To account for these different possible sentence terminations, I use the following regular expression: `' *[\.\?!][\'"\)\]]* *'` which states that a sentence may end in .?! and may be followed by one or none of these signs: ' or " ) or ] .  
 
 I use the regular expression module in python `re` to `findall` the elements that match my regular expression in the line. After this, I count how many of these matching exist and add the count to the `no_sentences` counter.
```python
 			no_sentences+=len(re.findall(r' *[\.\?!][\'"\)\]]* *', line))
```

To print the results for *Number of sentences* I convert the counter to a string and print it as follows:
```python
print('Sentences: '+ str(no_sentences))
```

With that we have complete the initial points of question 1, now let's get the brownie points.

First to be able to read the input file from the command line, I import the [sys](https://docs.python.org/3/library/sys.html) module, which provides access to some variables used or maintained by the interpreter. Specifically we need the command line arguments: `sys.argv` . 

In the code, I check if a file name was provided in the command line by checking the *length* of `sys.argv` and if a argument was provided this is assigned to the variable `inFile` (Used in the open loop). Note, this can be performed in a more robust way, checking if the argument is in the format we need, but to lack of time I did not do the extra checks. If no argument is provided then we use a default inFile called Test.txt.
def main():	
```python
	if len(sys.argv) > 1:
		inFile = sys.argv[1]
	else:
		inFile = 'Test.txt'
```
Next to calculate the average sentence length in words. I create a list of the sentences in the file by splitting the line every time the regular expression is found. This time I perform that different from the sentence count before, because I want to actually save the sentence into a list `sentenceList`. 
```python
sentenceEnders = re.compile(r' *[\.\?!][\'"\)\]]* *')
			sentenceList += sentenceEnders.split(line)
```
After the list of sentences is generated, I loop through the sentenceList and count the number of words per sentence. To do this I split the sentence every white space and append the count to a variable names `wordcounts` after creating the list of number of words per sentence, I get the average and save it to `average_wordcount`.

```python
#Get average # words per sentence
	wordcounts=[] # per sentence
	for sentence in sentenceList:
		words2 = sentence.split(' ')
		wordcounts.append(len(words2))
	average_wordcount = sum(wordcounts)/len(wordcounts)
```
Next I display the results for average word count per sentence:
```python
print('Avg. Word Count: '+ str(average_wordcount))
```

The last brownie point I did (I started running out of time to start problem 2), I created the list of words used and ordered them in descending frequency. First to obtain the frequency of each word, I loop through the word list and append to wordfreq the count of each word using the [count()](https://www.tutorialspoint.com/python/list_count.htm) function. After we form a numpy array with the words and the frequency of the words.
```python
#Frequency of words
	wordfreq = []
	for w in words:
		wordfreq.append(words.count(w))
	WordFreq=np.column_stack((words, wordfreq))
  ```
  Next I display the WordFrequency list and sort it in the display (The sort command works in Python 3.5). Here I was almost out of time for problem 2, so I did not have a chance to remove the repeated values.  
```python
  print(np.sort(WordFreq))
```
  
With that I concluded Question 1, an example run command and results are:
```python  
python Question1.py Test2.txt
  
Total word count: 10
Unique words: 6
Sentences: 4
Avg. Word Count: 2.2
Words Used and their Frequency:
[['4' 'adri']
 ['4' 'adri']
 ['4' 'adri']
 ['4' 'adri']
 ['1' 'adri.']
 ['2' 'dos']
 ['2' 'dos']
 ['1' 'dos.']
 ['1' 'tres.']
 ['1' 'cuatro.']]
  ```
___
## Question 2

Suppose we have 2 tables called Orders and Salesperson shown below:

Sales Person

| ID | Name | Age | Salary |
| ------------- |:-------------:|:-------------:| -----:|
| 1 | Abe | 61 | 140000|
| 2 | Bob | 34 | 44000 |
| 5 | Chris | 34 | 40000 |
| 7 | Dan | 41 | 52000 |
| 8 | Ken | 57 | 115000 |
| 11 | Joe | 38 | 38000|


Orders

| Number | order_date | cust_id | salesperson_id | Amount |
| ------------- |:-------------:|:-------------:|:-------------:|-----:|
| 10 | 8/2/96 | 4 | 2 | 540 |
| 20 | 1/30/99 | 4 | 8 | 1800 |
| 30 | 7/14/95 | 9 | 1 | 460 |
| 40 | 1/29/98 | 7 | 2 | 2400 |
| 50 | 2/3/98 | 6 | 7 | 600 |
| 60 | 3/2/98 | 6 | 7 | 720 |
| 70 | 5/6/98 | 9 | 7 | 150 |

Write a SQL query that retrieves the names of all salespeople that have more than 1 order from the tables above. You can assume that each salesperson only has one ID.

___
My code for this question is found [here](https://github.com/adrifloresm/DataChallenge/blob/Draft/Question2.ipynb)

For this question I only had a few minutes left, so I decided to complete it in Python Pandas (I am most familiar with it) to complete it faster. 

First, I create the dataframes for the two tables:
```python
Salesperson= pd.DataFrame([{'ID': 1, 'Name' : 'Abe', 'Age:': 61, 'Salary': 140000},
{'ID': 2, 'Name' : 'Bob', 'Age:': 34, 'Salary': 44000},
{'ID': 5, 'Name' : 'Chris', 'Age:': 34, 'Salary': 40000},
{'ID': 7, 'Name' : 'Dan', 'Age:': 41, 'Salary': 52000},
{'ID': 8, 'Name' : 'Ken', 'Age:': 57, 'Salary': 115000},
{'ID': 11, 'Name' : 'Joe', 'Age:': 38, 'Salary': 38000}])

df=pd.DataFrame([
        {'Number': 10, 'order_date': 8/2/96,'cust_id': 4, 'Salesperson_id': 2, 'Amount': 540},
        {'Number': 20, 'order_date': 1/30/99,'cust_id': 4, 'Salesperson_id': 8, 'Amount': 1800},
        {'Number': 30, 'order_date': 7/14/95,'cust_id': 9, 'Salesperson_id': 1, 'Amount': 460},
        {'Number': 40, 'order_date': 1/29/98,'cust_id': 7, 'Salesperson_id': 2, 'Amount': 2400},
        {'Number': 50, 'order_date': 2/3/98,'cust_id': 6, 'Salesperson_id': 7, 'Amount': 600},
        {'Number': 60, 'order_date': 3/2/98,'cust_id': 6, 'Salesperson_id': 7, 'Amount': 720},
        {'Number': 70, 'order_date': 5/6/98,'cust_id': 9, 'Salesperson_id': 7, 'Amount': 150}])
```

Next, to obtain all the sale person Ids that have more than 1 order, I obtain the frequency of each Salesperson_id in the Orders dataframe which I named df (In time crunch I forgot to name it Orders).
```python
freq=df['Salesperson_id'].value_counts()
```

After this, I drop all the IDs that have less than 2 frequencies and save that into `Ids`. Next I reset the Index of `Ids` to be able to access the actual Id numbers to be able to select the name in the Salesperson dataframe.
```python
Ids=freq.where(freq>1).dropna()
a=Ids.reset_index()
```

Next I loop through the Ids `a['index']` , for each Id I search the Salesperson dataframe ID column that matches the current ID, I obtain the Name from that specific entry and add it to a list names. Note here it is important to perform `dropna()` because when we use the `where` function it returns a Boolean mask  with NaN where the condition was not met, also it is important to use `item()` to only return the item of `Salesperson['Name']` and not the pandas object.
```python
names=[]
for i in a['index']:
    names.append(Salesperson['Name'].where(Salesperson['ID'] == i ).dropna().item())
```
After this I print the Salespersons Name from the names list created in the previous step, as follows.
```python
print('The names are: ' + str(names))
```

Which prints the result for Question 2:
The names are: ['Dan', 'Bob']

That completed my data challenge. Flock thanks for this great experience!
