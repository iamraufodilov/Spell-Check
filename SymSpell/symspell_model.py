# load libraries
from collections import Counter
from sklearn.datasets import fetch_20newsgroups
import re
from symspellpy import SymSpell


#load dataset
# and create corpus
corpus = []
for line in fetch_20newsgroups().data:
    line = line.replace('\n', ' ').replace('\t', ' ').lower()
    line = re.sub('[^a-z ]', ' ', line)
    tokens = line.split(' ')
    tokens = [token for token in tokens if len(token) > 0]
    corpus.extend(tokens)

corpus = Counter(corpus)
corpus_dir = 'G:/rauf/STEPBYSTEP/Projects/NLP/Spell Check/SymSpell/'
corpus_file_name = 'spell_check_dictionary.txt'
symspell = SymSpell(verbose=10)
symspell.build_vocab(
    dictionary=corpus, 
    file_dir=corpus_dir, file_name=corpus_file_name)

symspell.load_vocab(corpus_file_path=corpus_dir+corpus_file_name)


# single word correction
results = symspell.correction(word='baraka obame')
print(results) # here we go edwarda corrected to barak obama 


# compound word correction
results = symspell.corrections(sentence='Hello I am barake obame')
print(results) # here we got correct sentence suggestion for wrong spelled sentence


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# CONCLUSION
'''
this is project of spell correcting
simple aproach : Symmetric Delete Spelling Correction (SymSpell)
we load dataset from sklearn and we made corpus dictionary with this dataset
then we load symspell model with corpus to check wrong written words
'''