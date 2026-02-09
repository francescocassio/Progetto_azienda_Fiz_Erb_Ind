import csv
import mysql.connector
from mysql.connector import Error

CSV_PATH = r"/Progetto_azienda_completo\progetto_az2\file_vari\fatture.csv"
DB_CONFIG = {
    "user": "root",
    "password": "",
    "host": "localhost",
    "database": "azienda_generation",
}

def to_float(x):
    s = str(x).strip().replace(",", ".")
    return float(s)

def importa_csv():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        print("Connection to DB successful")
    except Error as e:
        print(f"Errore connessione DB: {e}")
        return

    insert_sql = """
        INSERT INTO fattura (
            emittente, destinatario, bene_servizio_venduto,
            importo, iva, imponibile, data_fattura
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    try:
        with open(CSV_PATH, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            colonne_richieste = {
                "emittente", "destinatario", "bene_servizio_venduto",
                "importo", "iva", "imponibile", "data_fattura"
            }
            missing = colonne_richieste - set(reader.fieldnames or [])
            if missing:
                raise ValueError(f"Mancano colonne nel CSV: {missing}")

            rows = []
            for r in reader:
                emittente = (r["emittente"] or "").strip() or "Azienda Zurich"
                destinatario = (r["destinatario"] or "").strip()
                bene = (r["bene_servizio_venduto"] or "").strip()
                importo = to_float(r["importo"])
                iva = to_float(r["iva"])
                imponibile = to_float(r["imponibile"])
                data_fattura = (r["data_fattura"] or "").strip()

                if not destinatario or not bene or not data_fattura:
                    raise ValueError(f"Riga non valida: {r}")

                rows.append((emittente, destinatario, bene, importo, iva, imponibile, data_fattura))

        cursor.executemany(insert_sql, rows)
        conn.commit()
        print(f"Import completato. Righe inserite: {cursor.rowcount}")

    except Exception as e:
        conn.rollback()
        print("Errore import:", repr(e))
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    importa_csv()
