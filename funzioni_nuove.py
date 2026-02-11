from funzioni_database import esegui_query_select
def mostra_clienti():
    r = esegui_query_select("select * from clienti")

    for elem in r:
        print(elem)

def id_clienti_presenti():
    r = esegui_query_select("select id_cliente from clienti")

    #trasformo la lista di tuple in lista di interi
    ris = []

    for elem in r:
        ris.append(elem[0])

    return ris

q_inserimento_fatture = """INSERT INTO fattura (bene_servizio_venduto, importo, iva, imponibile, data_fattura, cliente_id) VALUES
('Consulenza IT', 1220.00, 220.00, 1000.00, '2025-05-14', 3),
('Sviluppo Web', 2500.00, 450.82, 2049.18, '2025-09-21', 1),
('Manutenzione Server', 450.50, 81.24, 369.26, '2025-11-02', 8),
('Licenza Software', 890.00, 160.49, 729.51, '2026-01-10', 5),
('Audit Sicurezza', 3200.00, 577.05, 2622.95, '2025-04-12', 2),
('Formazione Personale', 1500.00, 270.49, 1229.51, '2025-07-30', 7),
('Backup Cloud', 120.00, 21.64, 98.36, '2025-08-15', 4),
('Supporto Tecnico', 650.00, 117.21, 532.79, '2025-12-05', 6),
('Analisi Dati', 2100.00, 378.69, 1721.31, '2025-03-22', 1),
('Consulenza IT', 980.00, 176.72, 803.28, '2025-06-18', 3),
('Sviluppo Web', 4300.00, 775.41, 3524.59, '2025-10-09', 8),
('Manutenzione Server', 350.00, 63.11, 286.89, '2025-11-28', 5),
('Licenza Software', 150.00, 27.05, 122.95, '2026-02-01', 2),
('Audit Sicurezza', 5000.00, 901.64, 4098.36, '2025-05-25', 4),
('Formazione Personale', 750.00, 135.25, 614.75, '2025-08-12', 6),
('Backup Cloud', 250.00, 45.08, 204.92, '2025-12-20', 7),
('Supporto Tecnico', 480.00, 86.56, 393.44, '2025-04-05', 3),
('Analisi Dati', 3150.00, 568.03, 2581.97, '2025-09-14', 1),
('Consulenza IT', 1100.00, 198.36, 901.64, '2025-11-11', 8),
('Sviluppo Web', 2850.00, 513.93, 2336.07, '2025-03-01', 5),
('Manutenzione Server', 560.00, 100.98, 459.02, '2026-01-15', 2),
('Licenza Software', 99.00, 17.85, 81.15, '2025-07-22', 4),
('Audit Sicurezza', 1800.00, 324.59, 1475.41, '2025-06-05', 6),
('Formazione Personale', 2200.00, 396.72, 1803.28, '2025-10-30', 7),
('Backup Cloud', 330.00, 59.51, 270.49, '2025-12-12', 1),
('Supporto Tecnico', 920.00, 165.90, 754.10, '2025-04-20', 3),
('Analisi Dati', 1250.00, 225.41, 1024.59, '2025-08-08', 8),
('Consulenza IT', 4100.00, 739.34, 3360.66, '2025-11-25', 5),
('Sviluppo Web', 1600.00, 288.52, 1311.48, '2026-02-05', 2),
('Manutenzione Server', 720.00, 129.84, 590.16, '2025-05-18', 4),
('Licenza Software', 450.00, 81.15, 368.85, '2025-09-29', 6),
('Audit Sicurezza', 2750.00, 495.90, 2254.10, '2025-12-01', 7),
('Formazione Personale', 1950.00, 351.64, 1598.36, '2025-03-15', 1),
('Backup Cloud', 85.00, 15.33, 69.67, '2025-06-25', 3),
('Supporto Tecnico', 1100.00, 198.36, 901.64, '2025-10-10', 8),
('Analisi Dati', 3400.00, 613.11, 2786.89, '2025-12-28', 5),
('Consulenza IT', 1350.00, 243.44, 1106.56, '2025-04-02', 2),
('Sviluppo Web', 550.00, 99.18, 450.82, '2025-08-22', 4),
('Manutenzione Server', 980.00, 176.72, 803.28, '2025-11-08', 6),
('Licenza Software', 2200.00, 396.72, 1803.28, '2026-01-20', 7),
('Audit Sicurezza', 4200.00, 757.38, 3442.62, '2025-05-30', 1),
('Formazione Personale', 600.00, 108.20, 491.80, '2025-09-05', 3),
('Backup Cloud', 190.00, 34.26, 155.74, '2025-12-15', 8),
('Supporto Tecnico', 340.00, 61.31, 278.69, '2025-03-10', 5),
('Analisi Dati', 2800.00, 504.92, 2295.08, '2025-07-12', 2),
('Consulenza IT', 1750.00, 315.57, 1434.43, '2025-11-18', 4),
('Sviluppo Web', 3900.00, 703.28, 3196.72, '2026-02-09', 6),
('Manutenzione Server', 1150.00, 207.38, 942.62, '2025-04-28', 7),
('Licenza Software', 670.00, 120.82, 549.18, '2025-08-01', 1),
('Audit Sicurezza', 2150.00, 387.70, 1762.30, '2025-10-25', 3);
"""


if __name__ == '__main__':
    id_clienti_presenti()