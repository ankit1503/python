# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

names_data_frame=pandas.read_csv("nato_phonetic_alphabet.csv")
# print(names_data_frame)
name_dict = {value.letter : value.code for (index, value) in names_data_frame.iterrows()}
print(name_dict)
name =input("Enter the name: ").upper()

# for letter in name:
#     print(name_dict[letter])

output_word = [name_dict[letter ] for letter in name]
print(output_word)