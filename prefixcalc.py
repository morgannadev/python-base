""" Calculadora prefix

Funcionamento:
[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
prefixcalc.py sum 5 2
7

prefixcalc.py mul 10 5
50

prefixcalc.py
operacao: sum
n1: 5
n2: 4
9

Os resultados serão salvos em `prefixcalc.log`.
"""

__version__ = "0.1.0"
__author__ = "Morganna Giovanelli"

import sys
import os
from datetime import datetime

arguments = sys.argv[1:]

# TODO: Exceptions
if not arguments:
    operation = input("operacao: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválido.")
    print("ex: sum 5 5")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operação inválida.")
    print("Operações válidas:", valid_operations)
    sys.exit(1)

validated_nums = []
for num  in nums:
    # TODO: Repetição while + exceptions
    if not num.replace(".", "").isdigit():
        print(f"Número inválido: {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

try:
    n1, n2 = validated_nums
except ValueError as error:
    print(str(error))
    sys.exit(1)

# TODO: Usar dict de funcoes
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

path = os.curdir
filepath = os.path.join(path, "prefixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

# print(f"{operation}, {n1}, {n2} = {result}", file = open(filepath, "a"))

print(f"O resultado é: {result}")

try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")
except PermissionError as error:
    # TODO: logging
    print(str(error))
    sys.exit(1)
