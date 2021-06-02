from textblob import TextBlob
misspelled_word= "Incorrct"
corrected_word= TextBlob(misspelled_word).correct()
print("Misspelled Word:",misspelled_word)
print("Corrected Word: ",corrected_word)

# you can also use list of misspelled words
print("========================================================")
misspelled_word_list=['Incorrct','Mang','Summay','Watr','Appl']
for word in misspelled_word_list:
    correct_word=TextBlob(word).correct()
    print("Misspelled Word:",misspelled_word_list)
    print("Corrected Word: ",correct_word)
