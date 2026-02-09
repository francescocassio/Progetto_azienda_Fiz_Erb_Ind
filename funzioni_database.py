import mysql.connector
import bcrypt
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="azienda_generation")
        print("Connection to DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def esegui_query(query):
    #creiamo la connessione al db
    connessione = create_connection()

    #creiamo un cursore per navigare nel db
    cursor = connessione.cursor()

    try:
        cursor.execute(query)
        connessione.commit() #committiamo i risultati
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
        connessione.close()




def esegui_query_select(query):
    #creiamo la connessione al db
    connessione = create_connection()

    #creiamo un cursore per navigare nel db
    cursor = connessione.cursor()

    try:
        cursor.execute(query)
        result = cursor.fetchall()

        return result
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
        connessione.close()

def esegui_query_param(query, param):
    connessione = create_connection()
    cursor = connessione.cursor()
    try:
        cursor.execute(query, param)
        connessione.commit()
        print("Query executed successfully")
        return cursor.rowcount

    except Error as e:
        print(f"The error '{e}' occurred")
        return 0

    finally:
        cursor.close()
        connessione.close()


def elimina_fattura(id_fattura: int) -> int:
    return esegui_query_param(
        "DELETE FROM fattura WHERE id_fattura = %s",(id_fattura,)
    )

def modifica_fattura(id_fattura: int, destinatario=None, bene_servizio_venduto=None, importo=None, iva=None, imponibile=None):
    campi = []
    valori = []

    if destinatario is not None:
        campi.append("destinatario = %s")
        valori.append(destinatario)

    if bene_servizio_venduto is not None:
        campi.append("bene_servizio_venduto = %s")
        valori.append(bene_servizio_venduto)

    if importo is not None:
        campi.append("importo = %s")
        valori.append(importo)

    if iva is not None:
        campi.append("iva = %s")
        valori.append(iva)

    if imponibile is not None:
        campi.append("imponibile = %s")
        valori.append(imponibile)

    if not campi:
        print("Non hai aggiornato niente")
        return 0

    query_update = f"UPDATE fattura SET {', '.join(campi)} WHERE id_fattura = %s"
    valori.append(id_fattura)
    righe = esegui_query_param(query_update, tuple(valori))
    return righe

def esegui_query_select_param(query, param):
    connessione = create_connection()
    cursor = connessione.cursor()

    if not isinstance(param, (tuple, list, dict)):
        param = (param,)

    try:
        cursor.execute(query, param)
        result = cursor.fetchall()
        return result

    except Error as e:
        print(f"The error '{e}' occurred")
        return []
    finally:
        cursor.close()
        connessione.close()

def trova_fattura_per_id(id_fattura: int):

    query_id = """
    
        SELECT id_fattura, emittente, destinatario, bene_servizio_venduto,
               importo, iva, imponibile, data_fattura
        FROM fattura
        WHERE id_fattura = %s
        
    """
    res = esegui_query_select_param(query_id, (id_fattura,))
    return res[0] if res else None


def spese_totali_per_cliente():
    query = """
        SELECT destinatario, SUM(importo) AS totale_speso
        FROM fattura
        GROUP BY destinatario
        ORDER BY totale_speso DESC
    """
    return esegui_query_select(query)

def incassi_totali():
    query = "SELECT COALESCE(SUM(importo), 0) FROM fattura" #ho chiesto la query a chat
    ris = esegui_query_select(query)
    return float(ris[0][0]) if ris else 0.0

import bcrypt
from mysql.connector import Error

def registra_utente(username: str, password: str, ruolo: str = "user") -> int:
    username = username.strip().replace(" ", "")
    if not username:
        raise ValueError("Username vuoto")

    if not password:
        raise ValueError("Password vuota")

    #ho chiesto come cryptare a chatgpt
    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    query = """
    
        INSERT INTO utenti (username, password_hash, ruolo)
        VALUES (%s, %s, %s)
        
    """

    return esegui_query_param(query, (username, password_hash, ruolo))

def login_utente(username: str, password:str):
    username = username.strip().replace(" ", "")
    if not username or not password:
        return None

    query = """

            SELECT id_utente, username, password_hash, ruolo FROM utenti where username = %s 

        """
    res = esegui_query_select_param(query, (username,))

    if not res:
        return None

    id_utente, user, password_hash, ruolo = res[0]

    check = bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8")) #grazie chat

    if not check:
        return None

    return {"id_utente": id_utente, "username": user, "ruolo": ruolo}

print("teo bosss")