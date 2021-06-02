# load libraries
import re
import string
from collections import Counter
import numpy as np
import itertools


# create function to create corpus
def read_corpus(filename):
  with open(filename, "r") as file:
    lines = file.readlines()
    words = []
    for line in lines:
      words += re.findall(r'\w+', line.lower())

  return words


#load dataset
words = read_corpus("G:/rauf/STEPBYSTEP/Projects/NLP/Spell Check/Spell Checker/big.txt")

# lets look dataset

#_>print(f"There are {len(words)} total words in the corpus")

vocabs = set(words)
#_>print(f"There are {len(vocabs)} unique words in the vocabulary") 

word_counts = Counter(words)
#_>print(word_counts["love"])

total_word_count = float(sum(word_counts.values()))
word_probas = {word: word_counts[word] / total_word_count for word in word_counts.keys()}
#_>print("look at two word nd their probability", dict(itertools.islice(word_probas.items(), 2)))
#_>print(word_probas["love"]) # here we can see love's probability in our whole text is 0.000433853090530977

# split the word
def split(word):
  return [(word[:i], word[i:]) for i in range(len(word) + 1)]
#_>print(split("trash"))


# delete the word
def delete(word):
  return [l + r[1:] for l,r in split(word) if r]
#_>print(delete("trash"))


# swap the word
def swap(word):
  return [l + r[1] + r[0] + r[2:] for l, r in split(word) if len(r)>1]
#_>print(swap("trash"))


# replace letters
def replace(word):
  letters = string.ascii_lowercase
  return [l + c + r[1:] for l, r in split(word) if r for c in letters]
#_>print(replace("trash"))


#insert letter
def insert(word):
  letters = string.ascii_lowercase
  return [l + c + r for l, r in split(word) for c in letters]
#_>print(insert("trash"))


# get all result into set which hold only unique word
def edit1(word):
  return set(delete(word) + swap(word) + replace(word) + insert(word))
#_>print(edit1("trash"))

def edit2(word):
  return set(e2 for e1 in edit1(word) for e2 in edit1(e1))
#_>print(edit2("trash"))


# crete function to check word is correct or correct the word
def correct_spelling(word, vocabulary, word_probabilities):
  if word in vocabulary:
    print(f"{word} is already correctly spelt")
    return 

  suggestions = edit1(word) or edit2(word) or [word]
  best_guesses = [w for w in suggestions if w in vocabulary]
  return [(w, word_probabilities[w]) for w in best_guesses]


# lets check our model
word = "famile"
corrections = correct_spelling(word, vocabs, word_probas)

if corrections:
  print(corrections)
  probs = np.array([c[1] for c in corrections])
  best_ix = np.argmax(probs)
  correct = corrections[best_ix][0]
  print(f"{correct} is suggested for {word}") # here we go we write famile but our model corrected it with first option "family" as second option "famine" 


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# CONCLUSION
'''
first we created vocabulary with big.txt file 
then we get word probability dictionary
then we apply fuctions delete, insert, swap, replace 
in last we corrected the word with function
'''