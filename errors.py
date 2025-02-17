import sys
import os

# EAFP - Easy to Ask Forgiveness than Permission
# É mais fácil pedir perdão do que permissão 

try:
    names = open("names.txt", encoding="utf-8").readlines()
except FileNotFoundError as e:
    print(f"[Error] {str(e)}")
    sys.exit(1)

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)