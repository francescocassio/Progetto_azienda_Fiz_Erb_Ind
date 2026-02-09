import mysql.connector

def crea_tabella_clienti():
    conn = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="azienda_generation")
    cursor = conn.cursor()

    q_crea_clienti = """
    create table clienti(
         id_cliente INT PRIMARY KEY,
         nome_cliente VARCHAR(80) NOT NULL,
         sede_cliente VARCHAR(80) NOT NULL
         
    )
"""
    cursor.execute(q_crea_clienti)

    q = """INSERT INTO clienti (id_cliente, nome_cliente, sede_cliente) VALUES  
            (1, 'Tecno Systems S.p.A.', 'Milano'),
            (2, 'Food&Co S.r.l.', 'Bologna'),
            (3, 'Green Energy S.p.A.', 'Roma'),
            (4, 'Logistica Rapida S.r.l.', 'Torino'),
            (5, 'SoftDev Solutions', 'Napoli'),
            (6, 'Arredi Design S.p.A.', 'Firenze'),
            (7, 'AutoParts Italia', 'Modena'),
            (8, 'Mediterranea Import', 'Palermo');
            """

    cursor.execute(q)
    conn.commit()
    cursor.close()
    conn.close()
if __name__ == '__main__':
    try:
        crea_tabella_clienti()
        print("tabella clienti creata con successo")
    except mysql.connector.errors.ProgrammingError:
        print("Tabella già esistente")
