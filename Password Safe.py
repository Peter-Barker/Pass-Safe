# This is a program which takes inputs consisting of a reference and password that the user wishes to record 
# and writes them to an external txt file.

# NOTE: ' os.system("cls") ' IS FOR WINDOWS ONLY
# NOTE: ' os.system("clean") ' IS FOR UNBUNTU ONLY

import time
import os

# This section determines the password of the folder and its protection

print("Peter's Password Safe" + "\n")
password = input("Enter your password to access the safe: " + "\n" + "\n" + ">")

if password == "peter":
  os.system("cls")
else:
    print("\n" "Incorrect password. The program will automatically close now.")
    time.sleep(3)
    quit()    

# This section determines whether the user desires to insert a new record, if they desire to view their records or if they want to exit.
# At the end of option 1 and 2 the program will return to the 'main menu' .

while True:
  print("Input a number to choose your action:" + "\n")
  input_1 = input("1 - view your records" + "\n" + "2 - add a new record" + "\n" + "3 - exit the program" + "\n" + "\n" + ">")
  os.system("cls")
  if input_1 == "1": 
    print("Press enter to return to the menu.")
    print("")
    print("")
    print("This is a list of your records:" + "\n")
    f = open("Record.txt", "r")
    print(f.read())
    input("")
    os.system("cls")
  elif input_1 == "2":
    REFERENCE = input("Enter a reference that you wish to record: ")
    PASSWORD = input("\n" "Enter the password you wish to record for this reference: ")
    f = open("Record.txt", "a")
    f.write("-" * 60 + "\n" + "Reference: " + REFERENCE + "\n" + "Password: " + PASSWORD + "\n")
    f.close()
    os.system("cls")
  else:
    quit()
