input_string = input("Введите строку: ")

input_string = input_string.lower()

if input_string == input_string[::-1]:
    print("yes")
else:
    print("no")