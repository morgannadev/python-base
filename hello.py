#!/usr/bin/env python3
"""Hello World Multi Línguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:
Tenha a variável LANG devidamente configurada. Ex:
    export LANG=pt_BR

Execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Morganna Giovanelli"
__licence__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello World"

if current_language == "pt_BR":
    msg = "Olá Mundo"
elif current_language == "it_IT":
    msg = "Ciao Mondo"

print(msg)