import random
import re #importing regex for string validation

entrants = list()

def name_validator(name):
    if re.findall('[A-Za-z]\s[A-Za-z]', name):# regex to match two words seperated by space
        if(len(name.split(" "))>2): # if more that 2 names return false aswell
            return False
        return True
    else:
        return False

def contact_validator(contact):
    if re.findall('^[0-9]{10,11}$', contact):# regex to match all numbers only with range 10/11 and no space
        return True
    else:
        return False

def email_validator(email):
    if (re.findall('^[a-z0-9]((\.|\+)?[a-z0-9]){1,}@gmail\.co.uk$', email) or re.findall('^[a-z0-9]((\.|\+)?[a-z0-9]){1,}@hotmail\.co.uk$', email)):# regex to match all emails that have atleast one character behind domain
        return True
    else:
        return False

    
while True:
    name = input("Enter participant name\n> ")
    if not name:
        break
    if not name_validator(name):
        print("Invalid name format!! \nCorrect format is: Fname Lname\n\n")
        continue
    phone = input("Enter participant contact number\n> ")
    if not contact_validator(phone):
        print("Invalid contact format!! \nCorrect format is all numbers with 10 or 11 digits \n\n")
        continue
    email = input("Enter participant email\n> ")
    if not email_validator(email):
        print("Invalid email format!! \nCorrect format is: something@gmail.co.uk or something@hotmail.co.uk\n\n")
        continue
    entrants.append([name, phone, email])

print("Competition Finished!")
winner = random.choice(entrants)
print("The winner is: {0}, contact number is: {1}, email adress is: {2}".format(winner[0], winner[1], winner[2]))
