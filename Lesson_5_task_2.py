word = input("Введите слово из латинских букв: ")

# Определение гласныых букв
vowel_a = 0
vowel_e = 0
vowel_i = 0
vowel_o = 0
vowel_u = 0
consonant_count = 0

# Подсчёт гласных и согласных
for char in word:
    if char == 'a':
        vowel_a += 1
    elif char == 'e':
        vowel_e += 1
    elif char == 'i':
        vowel_i += 1
    elif char == 'o':
        vowel_o += 1
    elif char == 'u':
        vowel_u += 1
    else:
        consonant_count += 1

# Проверка наличия хотя бы какой-то буквы из перечисленных
if vowel_a == 0 and vowel_e == 0 and vowel_i == 0 and vowel_o == 0 and vowel_u == 0:
    print(False)
else:
    total_vowels = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u
    print(f"Количество гласных: {total_vowels}")
    print(f"Количество согласных: {consonant_count}")
    print(f"Количество 'a': {vowel_a if vowel_a > 0 else False}")
    print(f"Количество 'e': {vowel_e if vowel_e > 0 else False}")
    print(f"Количество 'i': {vowel_i if vowel_i > 0 else False}")
    print(f"Количество 'o': {vowel_o if vowel_o > 0 else False}")
    print(f"Количество 'u': {vowel_u if vowel_u > 0 else False}")