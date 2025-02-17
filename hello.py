#!/usr/bin/env python3
"""Hello World Multi Línguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:
Tenha a variável LANG devidamente configurada. Ex:
    export LANG=pt_BR

Ou informe através do CLI argument `--lang`
Ou o usuário terá que digitar.

Execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Morganna Giovanelli"
__licence__ = "Unlicense"

import os
import sys 
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# nossa instancia
log = logging.Logger("logs.py", log_level)

# level
ch = logging.StreamHandler() # ch = console handler
ch.setLevel(log_level)

# formatação
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)

# destino
log.addHandler(ch)

arguments = {
    "lang": None,
    "count": 1,
}
for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use `=`, you passed %s, try --key=value: %s",
            arg,
            str(e)
        )
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid option: `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language: ")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, le Monde!",
}

# try com valor default
# message = msg.get(current_language, msg["en_US"])

message = ""
try:
    message = msg[current_language]
except KeyError as error:
    print(f"[Error] {str(error)}")
    print(f"Language {current_language} is invalid. Choose from: {list(msg.keys())}")

print(message * int(arguments["count"]))