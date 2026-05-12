import string
password = input("enter your password ")
upper_case =  any([1 if c in string.ascii_uppercase else 0  for c in password])
lower_case_case =  any([1 if c in string.ascii_lowercase else 0  for c in password])
special_case =  any([1 if c in string.punctuation else 0  for c in password])
digits_case =  any([1 if c in string.digits else 0  for c in password])

characters = [upper_case, lower_case_case, special_case, digits_case]
length = len(password)

score= 0
with open("commonpass.txt", "r", encoding="utf-8") as f:
    common = f.read().splitlines()

if password in common:
    print("this password is common, score = 0","/7")
    exit()

if length >= 8:
    score += 1
if length>= 12:
    score +=1
if length >= 17:
    score +=1
if length >= 24:
    score +=1

for character in characters:
    if character:
        score += 1
if score <4:
    print("weak password", score,"/7")
if score >=4 and score <6:
    print("medium password", score,"/7")
if score >=6:
    print("strong password", score,"/7")




#print("lower_case",lower_case_case)
#print("specialcase",special_case)
#print("digits_case",digits_case)
#print("upper_case",upper_case)
#print("score", score)

