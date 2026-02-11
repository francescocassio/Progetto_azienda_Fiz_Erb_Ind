import datetime
import mysql.connector
from funzioni_database import create_connection,esegui_query_param, esegui_query_select
from funzioni_database import elimina_fattura
from funzioni_database import trova_fattura_per_id
from funzioni_database import modifica_fattura
from funzioni_database import spese_totali_per_cliente
from funzioni_database import incassi_totali
from funzioni_database import login_utente
#NON VA LO STESSOOOOOO. from getpass import getpass #chiesto a chatgpt come nascondere i caratteri della password all'inserimento
from funzioni_database import registra_utente
from funzioni_nuove import mostra_clienti, id_clienti_presenti


def inserisci_fattura():

    risultato = esegui_query_select("SELECT MAX(id_fattura) FROM fattura")
    id_massimo = risultato[0][0]

    id_fattura = (id_massimo if id_massimo is not None else 0) + 1 #AIUTO GEMINI (calcolo se id è nullo perchè 0 fatture, lo trasforma in 0)
    mostra_clienti()

    while True:
        destinatario_id = int(input("Inserisci l'id del destinatario: "))
        if destinatario_id in id_clienti_presenti():
            break
        else:
            print("Inserisci un id valido!")


    bsvenduto = input("Inserisci il bene servizio venduto: ").strip()

    try:
        importo = float(input("Inserisci l'importo: "))
    except:
        print("Errore: L'importo deve essere un numero valido. Operazione annullata.")
        return

    if bsvenduto == "":
        print("Errore: Servizio mancanti. Operazione annullata.")
        return

    imponibile = importo / 1.22

    iva = importo - imponibile

    #impostiamo come data di fattura direttamente la data odierna in cui la stiamo registrando
    data_fattura = datetime.date.today()

    # impacchettiamo tutti i dati in una tupla, per passarla in allegato alla execute
    dati = (id_fattura, bsvenduto, importo, iva, imponibile, data_fattura, destinatario_id)

    q_inserisci_fattura = f"""
    INSERT INTO fattura (id_fattura,bene_servizio_venduto, importo, iva, imponibile, data_fattura, cliente_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    esegui_query_param(q_inserisci_fattura, dati)

    print("Complimenti, fattura inserita!")


def mostra_fatture():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM fattura")

    print("--- ELENCO FATTURE ---")

    #qui non usiamo fetchall cosi leggiamo i dati al volo e li visualizziamo
    print(f"{'id_fattura':<12}{'emittente':<20}{'destinatario':<15}{'bene/servizio':<15}{'importo':<10}{'IVA':<10}{'imp':<10}{'data':<15}")
    for f in cursor:
        print(f"{f[0]:<12}{f[1]:<20}{f[2]:<15}{f[3]:<15}{f[4]:<10}{f[5]:<10}{f[6]:<10}{str(f[7]):<15}")

    cursor.close()
    conn.close()

def esegui_elimina_fattura():
    id_fattura = int(input("Seleziona ID fattura: "))
    righe = elimina_fattura(id_fattura)
    print("Nessuna fattura trovata" if righe == 0 else "Fattura eliminata")



def esegui_modifica_fattura():
    id_fattura = int(input("Seleziona ID fattura da modificare: "))
    fattura = trova_fattura_per_id(id_fattura)


    if not fattura:
        print(f"Nessuna fattura trovata con id = {id_fattura}.")
        return

    destinatario = input("Nuovo destinatario: ").strip() or None
    bene = input("Nuovo bene/servizio venduto: ").strip() or None
    importo_nuovo = input("Nuovo importo: ")



    importo = None
    iva = None
    imponibile = None

    if importo_nuovo:

        try:
            importo = float(importo_nuovo.replace(",", "."))
            imponibile = importo / 1.22

            iva = round((importo - imponibile),2)

        except ValueError:
            print("Importo non valido.")
            return
    righe = modifica_fattura(id_fattura, destinatario, bene, importo, iva, imponibile)

    print("Fattura modificata! " if righe > 0 else "Nessuna modifica effettuata")

def esegui_spese_totali_per_cliente():
    righe = spese_totali_per_cliente()

    if not righe:
        print("Nessun dato trovato.")
        return

    print("\n--- Spese totali per cliente (destinatario) ---")

    for destinatario, totale in righe:
        print(f"{destinatario}: {float(totale):.2f} €")

def esegui_incassi_totali():
    totale = incassi_totali()
    print(f"Incassi totali (somma importi fatture): {totale:.2f} €")


def esegui_registrazione():
    username = input("Scegli username: ").strip()

    password = input("Scegli password: ")
    conferma = input("Conferma password: ")

    if password != conferma:
        print("Le password non coincidono.")
        return

    try:

        righe = registra_utente(username, password, "user")
        if righe > 0:
            print("Utente registrato con successo")
        else:
            print("Registrazione non riuscita.")

    except mysql.connector.errors.IntegrityError:
        print("Username già esistente.")

    except ValueError as e:
        print(f"Errore: {e}")

    except Exception as e:
        print("Errore imprevisto:", repr(e))

def esegui_login():
    username = input("Inserisci il tuo username: ")
    password = input("Inserisci la password: ").strip().replace(" ", "")
    utente = login_utente(username, password)
    if not utente:
        print("CREDENZIALI ERRATE.")
        return None

    print(f"LOGIN EFFETTUATO. BENVENUTO {utente['username']}!")
    return utente

if __name__ == '__main__':
    inserisci_fattura()