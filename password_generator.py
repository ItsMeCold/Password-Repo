
import random
import string


def generate_password(min_Length, numbers = True , special_characters =  True):
    
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters+=special
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_Length:
        new_char = random.choice(characters)
        pwd+= new_char

        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = has_special and meets_criteria
    return pwd
min_Length = int(input("Enter min number length : "))
has_number = input("Should password have numbers? Y/N: ").upper() == "Y"
has_special = input("Should it have special char? Y/N? : ").upper() == "Y"
passs = generate_password(min_Length, has_number, has_special)
print("here is your pasword", passs)

    





