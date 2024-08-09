def display_elements(sequence):
    if sequence:
        print(sequence[0])
        display_elements(sequence[1:])
    else:
        print("Конец списка")

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
display_elements(my_list)