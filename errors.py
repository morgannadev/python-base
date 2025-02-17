import sys
import os

# LBYL: Look Before You Leap - Olhar antes de executar

if os.path.exists("names.txt"):
    print("O arquivo existe")
    input("...") # Race condition
    names = open("names.txt", encoding="utf-8").readlines()
else:
    print("[Error] File names.txt not found")
    sys.exit(1)

if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in the list")
    sys.exit(1)