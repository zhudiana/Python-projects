import pandas


#TODO 1. Create a dictionary in this format:

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.iloc[0]:row.iloc[1] for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
final_result = [data_dict[letter] for letter in word]
print(final_result)


