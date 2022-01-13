import pandas
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

all_letters = {row.letter: row.code for (index, row) in nato_data.iterrows()}

word = input("Enter a word: ")
word_letters = [all_letters[item.upper()] for item in word]
print(word_letters)
