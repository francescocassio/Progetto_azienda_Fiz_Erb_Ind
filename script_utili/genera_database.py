import mysql.connector
def crea_database():
    conn = mysql.connector.connect(
        user="root",
        password="",
        host="localhost")
    cursor = conn.cursor()

    q_delete_database = "DROP DATABASE if exists azienda_generation"
    cursor.execute(q_delete_database)


    q_crea_database = "CREATE DATABASE azienda_generation"
    cursor.execute(q_crea_database)

if __name__ == '__main__':
    try:
        crea_database()
        print("Database creato con successo")
    except mysql.connector.errors.DatabaseError:
        print("Il database è già esistente")

print("ciaooooooooo")