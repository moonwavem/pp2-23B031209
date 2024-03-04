from itertools import permutations

def print_permutations():
    input_string = input("Введите строку: ")
    permuted_strings = permutations(input_string)
    for permuted_string in permuted_strings:
        print(''.join(permuted_string))

print_permutations()
