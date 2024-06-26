# -*- coding: utf-8 -*-

import os
import moduli.Funzioni as Funzioni
PERCORSOCSV = 'OrarioTabellaGlobale.csv'  # Percorso del file CSV dell'orario globale
PERCORSODIR = 'FileCreati'  # Directory in cui verranno creati i file di output
SCELTAMESSAGGIO = 'Operazione da eseguire: '  # Messaggio per richiedere l'operazione da eseguire
ERROREMESSAGGIO = 'Operazione non prevista.'   # Messaggio di errore per input non valido
FILENOTFOUND = 'File CSV non trovato!'  # Messaggio di errore per file CSV non trovato
SCELTE_VALIDE = ('0', '1', '2', '3', '4')  # Tuple delle scelte valide per il menu

# Pulisce la console per una visualizzazione più pulita
os.system('CLS')


uscita = False
while (not(uscita)):
    # Verifica se la directory specificata esiste, altrimenti la crea
    if (os.path.exists(PERCORSODIR)):
        pass
    else:
        os.system('md ' + PERCORSODIR)
    
    print('-' * 80)
    Funzioni.vociMenu()  # Stampa le voci del menu chiamando la funzione da Funzioni.py
    print('-' * 80)

    scelta = input(SCELTAMESSAGGIO)  # Richiede all'utente di inserire una scelta
    while (scelta not in SCELTE_VALIDE):  # Continua a richiedere finché l'input non è valido
        print(ERROREMESSAGGIO)
        scelta = input(SCELTAMESSAGGIO)
    
    if scelta == SCELTE_VALIDE[0]:  # Se la scelta è '0', esci dal ciclo
        uscita = True

    elif scelta == SCELTE_VALIDE[1]:  # Se la scelta è '1', esegui la prima operazione
        if not(os.path.exists(PERCORSOCSV)):
            print(FILENOTFOUND)  # Se il file non esiste, stampa un messaggio di errore
            break
        else:
            filecsv = open(PERCORSOCSV, 'r')  # Apre il file CSV in modalità lettura

        righecsv = []
        classi = set()

        # Legge ogni riga del file CSV e costruisce un insieme delle classi presenti
        rigacsv = filecsv.readline().rstrip().split(',')
        while rigacsv != ['']:
            righecsv.append(rigacsv)
            rigacsv = filecsv.readline().rstrip().split(',')

        for i in range(len(righecsv)):
            for j in range(len(righecsv[i])):
                if (len(righecsv[i][j].strip(" ")) == 3 and righecsv[i][j] != ''):
                    classi.add(righecsv[i][j])
        
        classi = list(classi)

        # Richiede all'utente di inserire la classe da controllare e la converte in maiuscolo
        classe = input('Inserisci la classe da controllare: ').upper()
        while (classe not in classi):
            print(ERROREMESSAGGIO)
            classe = input('Inserisci la classe da controllare: ').upper()

        PERCORSOTXT = PERCORSODIR + '\\' + classe + '.txt'  # Percorso del file di output per la classe
        filetxt = open(PERCORSOTXT, 'a')  # Apre il file di output in modalità append
        filetxt.close()
        filetxt = open(PERCORSOTXT, 'w')  # Apre il file di output in modalità scrittura

        docenti_classe = Funzioni.elencoDocentiClasse(righecsv, classe)  # Ottiene gli insegnanti per la classe

        for i in docenti_classe:
            filetxt.write(i + '\n')  # Scrive ciascun insegnante nel file di output
        
        filecsv.close()  # Chiude il file CSV
        filetxt.close()  # Chiude il file di output

# termine codice per lo svolgimento della prima scelta

    elif scelta == SCELTE_VALIDE[2]:  # Se la scelta è '2', esegui la seconda operazione
        if not(os.path.exists(PERCORSOCSV)):
            print(FILENOTFOUND)  # Se il file non esiste, stampa un messaggio di errore
            break
        else:
            filecsv = open(PERCORSOCSV, 'r')  # Apre il file CSV in modalità lettura

        righecsv = []
        docenti = []

        # Legge ogni riga del file CSV e costruisce una lista dei docenti presenti
        rigacsv = filecsv.readline().rstrip().split(',')
        while rigacsv != ['']:
            righecsv.append(rigacsv)
            rigacsv = filecsv.readline().rstrip().split(',')

        for i in range(len(righecsv)):
            docenti.append(righecsv[i][0].strip(' '))
        
        docenti.remove(docenti[0])
        docenti.remove(docenti[0])

        # Richiede all'utente di inserire il docente da controllare e lo converte in maiuscolo
        docente = input('Inserisci il docente da controllare: ').upper()
        while (docente not in docenti):
            print(ERROREMESSAGGIO)
            docente = input('Inserisci il docente da controllare: ').upper()

        PERCORSOTXT = PERCORSODIR + '\\' + docente + '.txt'  # Percorso del file di output per il docente
        filetxt = open(PERCORSOTXT, 'a')  # Apre il file di output in modalità append
        filetxt.close()
        filetxt = open(PERCORSOTXT, 'w')  # Apre il file di output in modalità scrittura

        orario_docente = Funzioni.orarioDocente(righecsv, docente)  # Ottiene l'orario del docente

        for i in righecsv[0]:
            filetxt.write(i + ', ')  # Scrive l'intestazione nel file di output
        filetxt.write('\n')
        
        for i in righecsv[1]:
            filetxt.write(i + ', ')  # Scrive l'orario del docente nel file di output
        filetxt.write('\n\n')

        ore_settimanali = 0
        for i in range(len(orario_docente)):
            filetxt.write(orario_docente[i] + ', ')  # Scrive l'orario del docente nel file di output
            if (orario_docente[i].strip() != ''):
                ore_settimanali += 1

        filetxt.write('\nNumero di ore settimanali: ' + str(ore_settimanali - 1))
        
        filecsv.close()  # Chiude il file CSV
        filetxt.close()  # Chiude il file di output

# codice per la terza scelta

    elif scelta == SCELTE_VALIDE[3]:  # Se la scelta è '3', esegui la terza operazione
        if not(os.path.exists(PERCORSOCSV)):
            print(FILENOTFOUND)  # Se il file non esiste, stampa un messaggio di errore
            break
        else:
            filecsv = open(PERCORSOCSV, 'r')  # Apre il file CSV in modalità lettura

        righecsv = []
        docenti = []

        # Legge ogni riga del file CSV e costruisce una lista dei docenti presenti
        rigacsv = filecsv.readline().rstrip().split(',')
        while rigacsv != ['']:
            righecsv.append(rigacsv)
            rigacsv = filecsv.readline().rstrip().split(',')

        for i in range(len(righecsv)):
            docenti.append(righecsv[i][0].strip(' '))
        
        docenti.remove(docenti[0])
        docenti.remove(docenti[0])

        # Richiede all'utente di inserire il docente da controllare e lo converte in maiuscolo
        docente = input('Inserisci il docente da controllare (D): ').upper()
        while (docente not in docenti):
            print(ERROREMESSAGGIO)
            docente = input('Inserisci il docente da controllare (D): ').upper()

        PERCORSOTXT = PERCORSODIR + '\\' + docente + ' (D)' + '.txt'  # Percorso del file di output per il docente
        filetxt = open(PERCORSOTXT, 'a')  # Apre il file di output in modalità append
        filetxt.close()
        filetxt = open(PERCORSOTXT, 'w')  # Apre il file di output in modalità scrittura

        ore_disponibili = Funzioni.oreDispDocente(righecsv, docente)  # Ottiene le ore disponibili del docente
        filetxt.write('Numero di ore disponibili di ' + docente + ': ' + str(ore_disponibili))

        filecsv.close()  # Chiude il file CSV
        filetxt.close()  # Chiude il file di output

    elif scelta == SCELTE_VALIDE[4]:  # Se la scelta dell'utente è quella di cercare docenti in base all'ora e al giorno
        if not(os.path.exists(PERCORSOCSV)):  # Se il file CSV non esiste
            print(FILENOTFOUND)  # Stampa un messaggio di file non trovato
            break  # Esce dal loop
        else:
            filecsv = open(PERCORSOCSV, 'r')  # Apre il file CSV in modalità lettura

        righecsv = []  # Lista vuota per memorizzare le righe del CSV
        giorni = []  # Lista per memorizzare i giorni presenti nel CSV
        ore = list(range(1, 8))  # Lista delle ore valide

        # Legge la prima riga del CSV e la splitta per ottenere una lista di intestazioni
        rigacsv = filecsv.readline().rstrip().split(',')
        while rigacsv != ['']:  # Continua fino a quando non raggiunge una riga vuota
            righecsv.append(rigacsv)  # Aggiunge la riga alla lista righecsv
            rigacsv = filecsv.readline().rstrip().split(',')  # Legge la riga successiva

        # Itera sulle intestazioni per estrarre i giorni e li aggiunge all'insieme 'giorni'
        for i in range(len(righecsv[0])):
            if (righecsv[0][i].strip() != '' and righecsv[0][i].strip() != 'Docente'):
                if (righecsv[0][i].strip() in giorni):
                    pass
                else:
                    giorni.append(righecsv[0][i].strip())

        giorni = list(giorni)  # Converte l'insieme in lista
        giorno = input(f'Inserisci il giorno da controllare {giorni}: ').capitalize()  # Chiede all'utente di inserire il giorno
        while (len(giorno) > 2 or giorno not in giorni):  # Verifica che il giorno inserito sia valido
            print(ERROREMESSAGGIO)  # Stampa un messaggio di errore
            giorno = input(f'Inserisci il giorno da controllare {giorni}: ').capitalize()  # Richiede il giorno

        ora = input(f'Inserisci l\'ora di {giorno} da controllare {ore}:')  # Chiede all'utente di inserire l'ora
        while (len(ora) > 1 or int(ora) not in ore):  # Verifica che l'ora inserita sia valida
            print(ERROREMESSAGGIO)  # Stampa un messaggio di errore
            ora = input(f'Inserisci l\'ora di {giorno} da controllare {ore}:')  # Richiede l'ora

        ora = int(ora)  # Converte l'ora in intero

        # Ottiene i dati dei docenti per il giorno e l'ora specificati
        dati = Funzioni.docentiGiornoOra(righecsv, giorno, ora)
        docenti_giorno_ora = dati[0]  # Lista dei docenti per il giorno e l'ora specificati
        ora = dati[1]  # Ora effettiva ottenuta dalla funzione

        # Crea il percorso del file di output per i docenti
        PERCORSOTXT = f'{PERCORSODIR}\\DOCENTI ({giorno}, {ora}a ora).txt'
        # Apre il file di output in modalità append
        filetxt = open(PERCORSOTXT, 'a')
        filetxt.close()  # Chiude il file
        # Apre il file di output in modalità scrittura
        filetxt = open(PERCORSOTXT, 'w')

        filetxt.write(f'Docenti con lezioni alla {ora}a ora di {giorno}\n')  # Scrive l'intestazione nel file di output

        # Itera sui docenti e li scrive nel file di output
        for i in docenti_giorno_ora:
            filetxt.write(i + '\n')

        filecsv.close()  # Chiude il file CSV
        filetxt.close()  # Chiude il file di output