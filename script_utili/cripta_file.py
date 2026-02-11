from cryptography.fernet import Fernet

# Nome del tuo file CSV di partenza e di quello criptato
file_csv_originale = "fatture.csv"
file_csv_criptato = "dati_criptati.csv"

# 1. Genera una chiave di crittografia
# ATTENZIONE: Questa chiave è fondamentale. Se la perdi, non potrai più decriptare il file!
chiave = Fernet.generate_key()

# Ti consiglio di salvare la chiave in un file separato e sicuro per poter decriptare in futuro
with open("chiave_segreta.key", "wb") as file_chiave:
    file_chiave.write(chiave)

# 2. Inizializza l'oggetto Fernet con la chiave generata
f = Fernet(chiave)

# 3. Leggi i dati dal file CSV originale (in modalità binaria "rb")
with open(file_csv_originale, "rb") as file:
    dati_file = file.read()

# 4. Cripta i dati
dati_criptati = f.encrypt(dati_file)

# 5. Salva i dati criptati in un nuovo file (sempre in modalità binaria "wb")
with open(file_csv_criptato, "wb") as file:
    file.write(dati_criptati)

print(f"File {file_csv_originale} criptato con successo in {file_csv_criptato}!")