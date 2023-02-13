special_char = [" ",".",",",";","-","'",'"']

def find_len_file_special(file_name):
    with open(file_name, 'r') as file:
        contents_res = ""
        contents = file.read()
        for i in contents:
            if i not in special_char:
                contents_res +=i
    return len(contents_res)

def find_len_file(file_name):
    with open(file_name, 'r') as file:
        contents = file.read()
    return len(contents)

def count_characters_special(file_name):
    with open(file_name, 'r') as file:
        contents = ""
        content = file.read()
        for i in content:
            if i not in special_char:
                contents +=i
        character_count = {}
        for char in contents:
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
        return character_count

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

def frequency_analysis(file_name):
    char_count = count_characters(file_name)
    total_chars = find_len_file(file_name)
    frequency_list = [(char, (count * 100) / total_chars) for char, count in char_count.items()]
    frequency_list.sort(key=lambda x: x[1], reverse=True)
    return frequency_list

file_name = r'/home/attacker/Desktop/newfile.txt'
frequency_list = frequency_analysis(file_name)
print("Character Frequency Analysis:")
for char, frequency in frequency_list:
    print(f"{char}: {frequency:.2f}%")

print("\nTotal Characters (including special characters):", find_len_file(file_name))
print("Total Characters (excluding special characters):", find_len_file_special(file_name))
