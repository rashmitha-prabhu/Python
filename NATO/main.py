import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic = {rows.letter: rows.code for (index, rows) in data.iterrows()}

name = input("Enter a word : ").upper()
phonetic = [nato_phonetic[letter] for letter in name]

print(phonetic)
