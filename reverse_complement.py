#This script writes a program that contains at least four functions.
# 1. It takes a DNA sequence from the user and ask if he/she wants to calculate the reverse, complement or reverse-complement, prints the answer on the screen.
# Detailed explanation and requirements:
# Asks the user for a DNA sequence. Checks the validity of the sequence.
#    a) If the sequence is invalid, prints the invalid base/bases with their positions and ask no more. 
#    b) If the sequence is valid, the program will continue with the following.
# Asks the user if s/he wants to print:  1) Reverse-complement
#                                          2) Complement
#                                          3) Reverse
#   Three functions find the reverse of the given sequence,find the complement of the given sequence and find the reverse-complement of the given sequence.
#   If the user gives an invalid input, the script gives a warning message and do not calculate the anything.

x = input("Please type a DNA sequence without spaces:").upper()
def sequence_validation(x): #this codes check if the sequence entered is correct or not
    bases = "ACTG" #it searches the sequences chars in ACTG
    count = 0 #count is used to determine the incorrect bases' positions
    list = [] #incorrect bases were appointed to a list to show them separately
    list_2 = [] #position of incorrect bases(count) were appointed to a list to show them separately
    z = -1 # this was used to concatenate the two list so we can show the base and its position together
    for var in x:
        count += 1
        if var not in bases:
            list.append(var)
            b = count
            list_2.append(b)

    for i in list_2:
        z = z + 1
        print(list[z] + "(base " + str(i) + ")" + " is not a valid base")

    if not list: #If our list that has incorrect bases were empty that meant our sequence was correct. Since it is more complicated to show the incorrect bases and their positions, I chose to display valid sequence message like this.
        print("This is a valid DNA sequence")
        w = input(
            "Would you like to print reverse-complement,complement, or reverse? \nPlease write:\n 1 one reverse-complement\n 2 for complement\n 3 for reverse \n 4 if you don't want to print anything:")
        print("You have chosen:", w)
        y = int(w) # since inputs are string, w was converted to integer. By if loop, each value of w was handled accordingly.
        if y == 1:
            def reverse_complement(x): #takes the complement of a sequence and reverses it #input x output reverse_comp
                bosh = [] # I decided to iterate through x and then appoint every base to a list
                for i in x.upper():
                    if i == "A":
                        zır = "T"
                        bosh.append(zır)
                    elif i == "G":
                        tır = "C"
                        bosh.append(tır)
                    elif i == "C":
                        mır = "G"
                        bosh.append(mır)
                    else:
                        kır = "A"
                        bosh.append(kır)

#since I appointed bases to a list, I had to concatenate them and create a string
                concenated_string_x = "" #our empty string
                for string in range(len(bosh)):
                    if string == len(bosh) - 1:
                        concenated_string_x += bosh[string]
                    else:
                        concenated_string_x += f'{bosh[string]}'
                reverse_comp = concenated_string_x[::-1] #it starts from the end towards the first taking each element. So it reverses a string
                print(reverse_comp)
                return reverse_comp
            reverse_complement(x)

        if y == 2:
            empty = []
            def bazcı(x): #finds the complement of a sequence #input x output concenated_string
                for i in x.upper():
                    if i == "A":
                        m = "T"
                        empty.append(m)
                    elif i == "G":
                        n = "C"
                        empty.append(n)
                    elif i == "C":
                        k = "G"
                        empty.append(k)
                    else:
                        j = "A"
                        empty.append(j)

            bazcı(x)
            concenated_string = ""
            for string in range(len(empty)):
                if string == len(empty) - 1:
                    concenated_string += empty[string]
                else:
                    concenated_string += f'{empty[string]}'
            print(concenated_string)
        if y == 3:
            def reverse(x): #finds the reverse of a sequence #input x output reverse
                kk = x.upper()
                reverse = kk[::-1] #it starts from the end towards the first taking each element. So it reverses a string
                print(reverse)
                return reverse
            reverse(x)

    else:
        print("This is not a valid DNA sequence")
        return x

sequence_validation(x)
