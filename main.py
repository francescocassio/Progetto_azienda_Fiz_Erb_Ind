from funzioni_supporto import scelta
from funzioni_servizio import esegui_login
from funzioni_servizio import esegui_registrazione
#permettere all'utente di inserire una nuova fattura, stando MOLTO attenti agli id sequenziali e
#a tutto ciò che non deve essere NULL. Inoltre pensate se riuscite ad inserire alcuni dei campi in
#automatico (imponibile, data, ecc)

#commento a caso test

#questo programma per funzionare necessita di un db chiamato azienda_generation e che mysql sia attivo

def main():
    utente = None
    while utente is None:
        print("1) Accedi")
        print("2) Registrati")
        print("3) Termina")

        try:
            x = int(input("scelta: "))
        except ValueError:
            print("Scelta non valida")
            continue

        if x == 1:
            utente = esegui_login()
        elif x == 2:
            esegui_registrazione()
        elif x == 3:
            print("ARRIVEDERCI")
            return

    scelta()

if __name__ == "__main__":
    main()

