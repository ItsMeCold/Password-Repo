import random
import time

generatorotp = random.randint(100000, 999999)

username = input("Username: ")
print("Hello there", username)
print("Here is your OTP for login:", generatorotp)
print("you have 15 seconds to enter the OTP")

start_time = time.time()
attempts = 3
while attempts >0:
  password = input("Enter your OTP: ")

  elapsed_time = time.time() - start_time

  if elapsed_time > 15:
      print("OTP Expired. Request a new OTP.")
    
  elif password == str(generatorotp):
      print("Login Successful")
  else:
      print("Login Failed")
      attempts -= 1
      print(f"Remaining attempts: {attempts}")