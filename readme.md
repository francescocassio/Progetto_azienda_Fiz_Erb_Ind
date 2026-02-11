# Progetto Gestione Fatturazione - Azienda Zurich

Questo repository contiene il sistema gestionale per la generazione, archiviazione e analisi delle fatture aziendali.

## 🛠️ Installazione e Setup

Per rendere il progetto operativo e configurare correttamente il database locale, è **obbligatorio** eseguire lo script di inizializzazione. Lo script si occuperà della creazione delle tabelle (`clienti` e `fattura`) e del popolamento iniziale dei record.

Esegui il seguente comando nel terminale:

```bash
python procedura_guidata_creazione.py
```

Il team di analisi ci richiede che il software che stiamo creando
possa permettere di esportare dei csv in questa forma:

id_fattura,sede_destinatario,bene_venduto,importo,data