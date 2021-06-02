from spellchecker import SpellChecker
spell=SpellChecker()
misspelled_word=spell.unknown(['Incorrct', 'Summry','Mondy','Spellng','Pyhon'])
print(type(misspelled_word))
for word in misspelled_word:
    print("Corrected word is ", spell.correction(word))
    print("Candidate words:",spell.candidates(word))
