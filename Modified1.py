special_char = [" ", ".", ",", ";", "-", "'", '"']
file_name = r'/workspaces/testtt/cipher.txt'


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

def frequency_analysis(file_name):
    char_count = count_characters(file_name)
    total_chars = find_len_file(file_name)
    frequency_list = [(char, round(count / total_chars, 4)) for char, count in char_count.items()]

    frequency_list.sort(key=lambda x: x[1], reverse=True)
    letter_map = {}
    print(frequency_list)
    for char, frequency in frequency_list:
        if frequency >= 0.1270:
            letter_map[char] = 'E'
        elif 0.0817 - 0.002 < frequency < 0.0817 + 0.002:
            letter_map[char] = 'A'
        elif 0.0150 - 0.002 < frequency < 0.0150 + 0.002:
            letter_map[char] = 'B'
        elif 0.0278 - 0.002 < frequency < 0.0278 + 0.002:
            letter_map[char] = 'C'
        elif 0.0425 - 0.002 < frequency < 0.0425 + 0.002:
            letter_map[char] = 'D'
        elif 0.0223 - 0.002 < frequency < 0.0223 + 0.002:
            letter_map[char] = 'F'
        elif 0.0202 - 0.002 < frequency < 0.0202 + 0.002:
            letter_map[char] = 'G'
        elif 0.0609 - 0.002 < frequency < 0.0609 + 0.002:
            letter_map[char] = 'H'
        elif 0.0697 - 0.002 < frequency < 0.0697 + 0.002:
            letter_map[char] = 'I'
        elif 0.0015 - 0.002 < frequency < 0.0015 + 0.002:
            letter_map[char] = 'J'
        elif 0.0077 - 0.002 < frequency < 0.0077 + 0.002:
            letter_map[char] = 'K'
        elif 0.0403 - 0.002 < frequency < 0.0403 + 0.002:
            letter_map[char] = 'L'
        elif 0.0241 - 0.002 < frequency < 0.0241 + 0.002:
            letter_map[char] = 'M'
        elif 0.0675 - 0.002 < frequency < 0.0675 + 0.002:
            letter_map[char] = 'N'
        elif 0.0751 - 0.002 < frequency < 0.0751 + 0.002:
            letter_map[char] = 'O'
        elif 0.0193 - 0.002 < frequency < 0.0193 + 0.002:
            letter_map[char] = 'P'
        elif 0.0010 - 0.002 < frequency < 0.0010 + 0.002:
            letter_map[char] = 'Q'
        elif 0.0599 - 0.002 < frequency < 0.0599 + 0.002:
            letter_map[char] = 'R'
        elif 0.0633 - 0.002 < frequency < 0.0633 + 0.002:
            letter_map[char] = 'S'
        elif 0.0906 - 0.002 < frequency < 0.0906 + 0.002:
            letter_map[char] = 'T'
        elif 0.0276 - 0.002 < frequency < 0.0276 + 0.002:
            letter_map[char] = 'U'
        elif 0.0098 - 0.002 < frequency < 0.0098 + 0.002:
            letter_map[char] = 'V'
        elif 0.0236 - 0.002 < frequency < 0.0236 + 0.002:
            letter_map[char] = 'W'
        elif 0.0015 - 0.002 < frequency < 0.0015 + 0.002:
            letter_map[char] = 'X'
        elif 0.0197 - 0.002 < frequency < 0.0197 + 0.002:
            letter_map[char] = 'Y'
        elif 0.0007 - 0.002 < frequency < 0.0007 + 0.002:
            letter_map[char] = 'Z'
        else:
            letter_map[char] = char
    return letter_map


frequency_list = frequency_analysis(file_name)
print("Character Frequency Analysis:")

for char, letter in frequency_list.items():
    print(f"{char} -> {letter}")
