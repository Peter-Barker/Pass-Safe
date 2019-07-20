# This is a program which takes inputs consisting of a reference and password that the user wishes to record 
# and writes them to an external folder

# NOTE: ' os.system("cls") ' IS FOR WINDOWS ONLY
# NOTE: ' os.system("clean") ' IS FOR UNBUNTU ONLY

import time
import os

# This section determines the password of the folder and its protection

password = input("Enter the password: ")

if password == "peter":
  os.system("cls")
else:
    print("\n" "Incorrect password. Please try again.")
    time.sleep(2)
    quit()    

# This section determines whether the user desires to reord a new REF/PASS or if they desire to view their records
# If they want to view their stored passwords, it should display them, either in an external file or in the terminal itself

print("Input a number to choose your action:" + "\n")
input_1 = input("1 - view your records" + "\n" + "2 - add a new record" + "\n" + "3 - exit the program" + "\n" + ">")
os.system("cls")

if input_1 == "1": 
  print("This is a list of your records:" + "\n")
  f = open("Record.txt", "r")
  print(f.read())
elif input_1 == "2":
  REFERENCE = input("Enter a reference that you wish to record: ")
  PASSWORD = input("\n" "Enter the password you wish to record for this reference: ")
  f = open("Record.txt", "a")
  f.write("\n" + "Reference: " + REFERENCE + "\n" + "Password: " + PASSWORD + "\n" + "--------------------------------------------------------------------")
  f.close()
else:
  quit()

print("")
input("Press enter to close the program")