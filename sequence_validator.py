#This script takes a DNA sequence from the user and prints it if the sequence is a valid sequence or not on the screen in the following format. Provides the user with the invalid character and its position for user's
#convenience. If there are several invalid bases, displays all of them.
#
#---Example for valid sequence:
#
#Please type a DNA sequence: TGTGAGTATGCTAGC
#This is a valid DNA sequence
#
#---Ex for invalid sequence:
#
#Please type a DNA sequence: TXGTCTYGACGGAC
#X (base 2) is not a valid base. 
#Y (base 7) is not a valid base.

x = input("Please type a DNA sequence without spaces:").upper()

def sequence_validation(x):
    bases = "ACTG"
    count = 0
    list = []
    list_2 = []
    z = -1
    for var in x:
        count += 1
        if var not in bases:
            list.append(var)
            b = count
            list_2.append(b)

    for i in list_2:
        z = z + 1
        print(list[z] + "(base " + str(i) + ")" + " is not a valid base")

    if not list:
        print("This is a valid DNA sequence")
    else:
        print("This is not a valid DNA sequence")
        return x


sequence_validation(x)


