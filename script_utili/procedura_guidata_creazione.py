from genera_database import crea_database
import time
from genera_tabella_clienti import crea_tabella_clienti
from genera_tabella import crea_tabella
from funzioni_nuove import q_inserimento_fatture

from funzioni_database import esegui_query

if __name__ == '__main__':
    crea_database()
    print("DB creato con successo")
    time.sleep(3)
    crea_tabella_clienti()
    print("Creata tabella clienti e popolata con 8 clienti")
    time.sleep(3)
    crea_tabella()
    print("Creata tabella fatture")
    esegui_query(q_inserimento_fatture)
    print("50 fatture inserite con successo")

