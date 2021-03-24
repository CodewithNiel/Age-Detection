'''
Author: Niel
Date: 20 March 2021
Purpose: Python Practice
'''

ageYear = int(input("What is your Age/Year of birth\n"))
isAge = False
isYear = False

if len(str(ageYear)) == 4:
    isYear = True

else:
    isAge = True


if (ageYear<1900 and isYear ):
    print("you are the oldest person alive")
    exit()

if (ageYear>2021):
    print("you are not yet born")
    exit()

if isAge:
    ageYear = 2021-ageYear

print(f"You will be 100 at {ageYear + 100}")

optional = int(input("Enter the year you want to know the age\n"))

print(f"You will be {optional - ageYear} at {optional}")
