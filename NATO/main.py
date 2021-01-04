import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic = {rows.letter: rows.code for (index, rows) in data.iterrows()}


def get_name():
    name = input("Enter a word : ").upper()
    try:
        phonetic = [nato_phonetic[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        get_name()
    else:
        print(phonetic)


get_name()
