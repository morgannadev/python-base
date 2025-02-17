#!/usr/bin/env python3

import os
import logging


# BOILERPLATE
# TODO: Usar função
# TODO: Usar lib loguru
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# nossa instancia
log = logging.Logger("logs.py", log_level)

# level
ch = logging.StreamHandler() # ch = console handler - Console/terminal/stderr
ch.setLevel(log_level)

# formatação
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)

# destino
log.addHandler(ch)

# log.debug("Mensagem para devs, qe, sysadmin")
# log.info("Mensagem geral para users")
# log.warning("Aviso que não causa erro")
# log.error("Erro que afena uma única execução")
# log.critical("Erro geral ex: banco de dados sumiu")

# print("---")

try:
    1/0
except ZeroDivisionError as error:
    log.error("Deu erro %s", str(error))
    #print(f"Deu erro {str(error)}")