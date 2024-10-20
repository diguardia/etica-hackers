import sys
import time
from bots.bot_no_sabe_encriptar import BotNoSabeEncriptar

# Probando nuestro bot (acá pueden cambiar la sibguiente línea por su bot para probarlo)
bot = BotNoSabeEncriptar()

texto_encriptado = bot.Encriptar("HOLA MUNDO", 3);
if texto_encriptado == "KSÑE PTQGS":
    print("Encriptar: Ok")
else:
    print("Encriptar: Error")

texto_descriptado = bot.Desencriptar("KSÑE PTQGS", 3);
if texto_descriptado == "HOLA MUNDO":
    print("Desencriptar: Ok")
else:
    print("Desencriptar: Error")

clave_inferida = bot.Romper("KSÑE PTQGS");
if clave_inferida == 3:
    print("Romper: Ok")
else:
    print("Romper: Error")