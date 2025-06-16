import pandas

#TODO 1. Create a dictionary in this format:
df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Type a word for conversion: ").upper()
    try:
        phonetic_list = [alphabet_dict[x] for x in word]
    except KeyError:
        print("Please type an a word. Only letters are acceptable.")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()