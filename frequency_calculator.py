# This script takes a DNA sequence as input and retuns a dictionary containing the total numbers of each base in the given sequence.
# The script does not check the validity of the DNA sequence.

userinput = input("Enter a sequence:").upper()
def frequency_calculator(seq):
    base_dictionary = {}
    for i in seq:
        base_dictionary[i] = base_dictionary.get(i, 0) + 1

    return base_dictionary

print(frequency_calculator(userinput))
