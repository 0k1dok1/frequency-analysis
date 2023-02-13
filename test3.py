special_char = [" ",".",",",";","-","'",'"']
file_name = r'C:\Users\lapislazuli\Desktop\cipher.txt'

def find_len_file(file_name):
    with open(file_name, 'r') as file:
        contents = file.read()
    return len(contents)

def count_characters(file_name):
    with open(file_name, 'r') as file:
        contents = file.read()
        character_count = {}
        for char in contents:
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
        return character_count
char_count = count_characters(file_name)

print("Character Count:")

frequency_list = [(char, round((count * 100) / find_len_file(file_name), 2)) for char, count in char_count.items()]
frequency_list.sort(key=lambda k: k[1], reverse=True)

# Add the specified characters and their frequency percentages to the output
fixed_frequency_list = [("E", 12.7), ("T", 9.1), ("A", 8.2), ("O", 7.5), 
                        ("I", 7.0), ("N", 6.7), ("S", 6.3), ("H", 6.1), 
                        ("R", 6.0), ("L", 4.0), ("D", 4.3), ("C", 2.8), 
                        ("U", 2.8), ("M", 2.4), ("W", 2.4), ("F", 2.2), 
                        ("G", 2.0), ("Y", 2.0), ("P", 1.9), ("B", 1.5), 
                        ("V", 1.0), ("K", 0.8), ("J", 0.2), ("X", 0.2), 
                        ("Q", 0.1), ("Z", 0.1)]

for char, freq in fixed_frequency_list:
    if char in char_count:
        print(char, str(freq) + "%", sep=":", end="\n")
    else:
        print(char, 0.0, "%", sep=":", end="\n")
