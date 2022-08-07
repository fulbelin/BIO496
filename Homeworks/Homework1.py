#This script:
# 1. takes an email address from the user,
# 2. iterates through the text,
# 3. records the position of sign @ into a variable called location_one 
# 4. records the position of sign . into a variable called location_two
# 5. by using string manipulations, detects the email provider from the input email and assign it into a variable called company_name,(the word between @ and . signs)
# 6. prints a message that says "Your email provider is company_name" (company_name is changeable).

x = str(input("Please enter your email adress:"))
count = 0
for i in x:
    count = count + 1
    if i == "@":
        location_one = "@"
        print("You have found @ : count is at:" + str(count))
        a = count
    if i == ".":
        location_two = "."
        print("You have found . : count is at:" + str(count))
        b = count

company_name = x[a:b - 1]
print("Your email provider is " + company_name)
