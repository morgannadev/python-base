"""Bloco de notas

notes.py new "Minha Nota"
tag: tech
text: 
Anotação geral sobre carreira de tecnologia.

notes.py read tech
...
"""
__version__ = '0.1.0'

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"You must specify subcommand {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print("Invalid command {arguments[0]}")

if arguments[0] == "read":
    #leitura das notas
    for line in open(filepath, encoding="utf-8"):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)

if arguments[0] == "new":
    #criação de novas notas
    title = arguments[1] # TODO: tratar exception
    text = [
        f"{title}",
        input("tag: ").strip(),
        input("text: ").strip(),
    ]
    # \t - tsv
    with open(filepath, "a", encoding="utf-8") as file_:
        file_.write("\t".join(text) + "\n")