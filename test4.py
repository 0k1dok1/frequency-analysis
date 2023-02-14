special_char = [" ", ".", ",", ";", "-", "'", '"']
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


# print(count_characters(file_name))

# def frequency_analysis(file_name):
#     char_count = count_characters(file_name)
#     total_chars = find_len_file(file_name)
#     frequency_list = [(char, (count * 100) / total_chars) for char, count in char_count.items()]
#     frequency_list.sort(key=lambda x: x[1], reverse=True)
#     return frequency_list

def frequency_analysis(file_name):
    char_count = count_characters(file_name)
    total_chars = find_len_file(file_name)
    frequency_list = [(char, round(count / total_chars, 4)) for char, count in char_count.items()]

    frequency_list.sort(key=lambda x: x[1], reverse=True)
    letter_map = {}
    print(frequency_list)
    for char, frequency in frequency_list:
        if frequency > 0.1270:
            letter_map[char] = 'E'
        elif frequency > 0.0906:
            letter_map[char] = 'T'
        elif frequency > 0.0817:
            letter_map[char] = 'A'
        elif frequency > 0.0751:
            letter_map[char] = 'O'
        elif frequency > 0.0697:
            letter_map[char] = 'I'
        elif frequency > 0.0675:
            letter_map[char] = 'N'
        elif frequency > 0.0633:
            letter_map[char] = 'S'
        elif frequency > 0.0609:
            letter_map[char] = 'H'
        elif frequency > 0.0599:
            letter_map[char] = 'R'
        elif frequency > 0.0403:
            letter_map[char] = 'L'
        elif frequency > 0.0425:
            letter_map[char] = 'D'
        elif frequency > 0.0278:
            letter_map[char] = 'C'
        elif frequency > 0.0241:
            letter_map[char] = 'M'
        elif frequency > 0.0276:
            letter_map[char] = 'U'
        elif frequency > 0.0202:
            letter_map[char] = 'G'
        elif frequency > 0.0193:
            letter_map[char] = 'P'
        elif frequency > 0.0150:
            letter_map[char] = 'B'
        elif frequency > 0.0098:
            letter_map[char] = 'V'
        elif frequency > 0.0077:
            letter_map[char] = 'K'
        elif frequency > 0.0015:
            letter_map[char] = 'J'
        elif frequency > 0.0010:
            letter_map[char] = 'Q'
        else:
            letter_map[char] = char
    return letter_map


frequency_list = frequency_analysis(file_name)
print("Character Frequency Analysis:")
# for char, frequency in frequency_list:
#     print(f"{char}: {frequency:.2f}%")

for char, letter in frequency_list.items():
    print(f"{char} -> {letter}")