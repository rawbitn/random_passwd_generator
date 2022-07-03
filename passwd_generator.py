import random

def generate_password(character_set):
    password = ''
    character_file = open(character_set, 'r+')
    character_array = character_file.readlines()
    len_character_array = len(character_array)
    for i in range(0, 8):
        raw = random.randint(0, len_character_array-1)
        password = str(password) + str(character_array[raw].rstrip('\n'))
    character_file.close()
    return password

#Example

file_name = "characters.txt"    # file name which contains the character list
print(generate_password(file_name))
