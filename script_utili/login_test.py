import bcrypt
from funzioni_database import esegui_query_param, esegui_query_param_noexc

import hashlib

from funzioni_database import esegui_query_select_param
def genera_hash_sha256(testo):
    # 1. Convertiamo la stringa in byte (necessario per l'hashing)
    dati_in_byte = testo.encode('utf-8')

    # 2. Creiamo l'oggetto hash SHA-256
    hash_object = hashlib.sha256(dati_in_byte)

    # 3. Otteniamo la rappresentazione esadecimale (leggibile)
    return hash_object.hexdigest()

username = input("Scegli username: ").strip()

password = input("Scegli password: ")

password_h = genera_hash_sha256(password)

q = "Select * from utenti where username = %s and password_hash = %s"
dati = (username, password_h)

r = esegui_query_select_param(q, dati)

print(r)


#username già esistente
#complessità maggiore della password
#criptare la password