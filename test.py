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

file_name = r'C:\Users\lapislazuli\Desktop\cipher.txt'
char_count = count_characters(file_name)
print("Character Count:")
for char, count in char_count.items():
    print(f"{char}: {count} :{round((count*100)/find_len_file(file_name),2)}""%")

print(find_len_file(file_name))
print(find_len_file(file_name))
