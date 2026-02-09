import mysql.connector
from mysql.connector import Error

def crea_tabella_utenti():
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="azienda_generation"
        )
        cursor = conn.cursor()

        q = """
        CREATE TABLE IF NOT EXISTS utenti (
            id_utente INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(50) NOT NULL UNIQUE,
            password_hash VARCHAR(255) NOT NULL,
            ruolo VARCHAR(20) NOT NULL DEFAULT 'user'
        );
        """
        cursor.execute(q)
        conn.commit()
        print("Tabella utenti OK (creata o già esistente).")

    except Error as e:
        print(f"Errore DB: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    crea_tabella_utenti()