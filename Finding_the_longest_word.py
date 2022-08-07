# This script finds the longest word in a given sentence.
# The built-in split() method in python is written on my own.

x = input("Please enter a sentence of minimum 3 words:")
white_space = []
count = 0
splitted_text = []
splinter = ''
for i in x:
   count += 1
   if i == ' ':
       a = count
       white_space.append(a)
       splitted_text.append(splinter)
       splinter = ''
   else:
       splinter += i
if splinter:
   splitted_text.append(splinter)

longest = 0
longest_word = []
length_word = []
for m in splitted_text:
    if len(m) > longest:
        longest = len(m)
        word = m
        longest_word.append(m)
        length_word.append(longest)

print("The longest word is " + word, "with the length of ", str(longest) + " letters")
