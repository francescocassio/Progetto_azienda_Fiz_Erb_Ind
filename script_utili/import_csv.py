import csv
import mysql.connector
from mysql.connector import Error

CSV_PATH = r"C:\Users\gianl\PycharmProjects\PythonProject\Progetto_azienda_completo\file_vari\fatture.csv"
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
            importo, iva, imponibile, data_fattura, cliente_id
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:
        with open(CSV_PATH, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            colonne_richieste = {
                "emittente", "destinatario", "bene_servizio_venduto",
                "importo", "iva", "imponibile", "data_fattura", "cliente_id"
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
                cliente_id = int(r["cliente_id"]) if r.get("cliente_id") else None
                if not destinatario or not bene or not data_fattura:
                    raise ValueError(f"Riga non valida: {r}")

                rows.append((emittente, destinatario, bene, importo, iva, imponibile, data_fattura, cliente_id))

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
