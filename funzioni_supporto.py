from funzioni_servizio import inserisci_fattura, mostra_fatture,esegui_elimina_fattura, esegui_modifica_fattura,esegui_spese_totali_per_cliente
from funzioni_servizio import esegui_incassi_totali,esegui_registrazione
def menu():
    #permette di salvare le fatture dopo averne chiesto i campi da riempire
    print("1) Salva fattura")

    #mostra tutte le fatture nel db
    print("2) Mostra fatture")

    print("3) Elimina fattura")

    print("4) Modifica fattura")

    print("5) Spese totali per cliente")

    print("6) Incassi totali")

    print("0) Termina")

def scelta():
    while True:
        menu()
        try:
            opzione = int(input("Scelta: "))

            if opzione == 1:
                inserisci_fattura()

            elif opzione == 2:
                mostra_fatture()

            elif opzione == 3:
                esegui_elimina_fattura()

            elif opzione == 4:
                esegui_modifica_fattura()

            elif opzione == 5:
                esegui_spese_totali_per_cliente()

            elif opzione == 6:
                esegui_incassi_totali()

            elif opzione == 0:
                break

            else:
                print("Opzione non valida")

        except ValueError:
            print("Campo non accettato")

        except EOFError:
            print("WTF? CTRL + d ma cosa combini")
            break

        except Exception as e:
            print("ERRORE dentro esegui_elimina_fattura:", repr(e))


if __name__ == '__main__':
    scelta()