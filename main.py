import arpWireless
import time
from dotenv import load_dotenv
import subprocess
import os
import msgBat

load_dotenv()
arppath = os.getenv("BATPATH")

def R1():
    print("Eseguendo la funzione R1.")
    print("! Devi eseguire questo comando su un computer. Sul mobile non funziona perché ci sono problemi con i permessi.")

    time.sleep(5)

    arpWireless.run_batch_file(batch_file_path="D:/Users/RedTy_ YT/Desktop/things/tools-per-dilettanti/windows/commandBats/arp.bat")
    print("Esecuzione completata.")
    print("""
    —————————————————————————————————————————————————————————————————————————————————————————————————————
          Vuoi che il tuo file sia cancellato?
          Digita 'si' per cancellare il file.
          Digita 'no' per non cancellare il file.
    —————————————————————————————————————————————————————————————————————————————————————————————————————
    """)
    while True:
        answer = input("> > >  ")
        if answer == "si":
            print("File cancellato")
            os.remove("responseArp.env")
            break
        elif answer == "no":
            print("Ok. Il file potrà anche essere salvato in un'altra posizione.")
            break
        else:
            print("Risposta non valida. Digita 'si' o 'no'.")
    main()


def R2():
    print("""TOOLS FOR NORMAL PERSONS :)
    Sei nella pagina 1 di aiuto. Per le altre pagine puoi digitare il comando 'help -{pagina che vuoi}'.
    —————————————————————————————————————————————————————————————————————————————————————————————————————
          COMANDI DISPONIBILI:
            'help'
            'ipconfig'
            'exit'
            'msg'
            'clear'
            'clearexit'
    —————————————————————————————————————————————————————————————————————————————————————————————————————
    Aiuto per il comando 'help':
    help -{comando} --> puoi digitare il comando 'help -{comando}' per avere informazioni sul comando richiesto.
    —————————————————————————————————————————————————————————————————————————————————————————————————————

    Aiuto per il comando 'ipconfig':
    help -ipconfig --> puoi digitare il comando 'help -ipconfig' per avere informazioni sul comando.
    """ + f"")


def R3():
    print("Aspetta...")
    time.sleep(3)
    print("""
    Per cambiare il path del file "arp.bat" sul tuo pc devi:
          1. Trovare il file "arp.bat";
          2. Andare nel file "Main.py" e andare alla riga 16;
          3. Tasto destro su "arp.bat" e seleziona "copia percorso";
          4. Incolla il percorso nella riga 16 del file Main.py.
    Dopo ciò potrai eseguire liberamente il comando 'ipconfig' sul tuo PC!
          !!! ATTENZIONE !!!
          | Gli slash nel path non devono essere così " \ " ma così " / ".
""")
    
def R4():
    print("Hai preso la versione standard del comando, senza opzioni.")
    user_input = input("Inserisci il ricevitore del messaggio (ip o *(tutti)). Se vuoi eliminare il comando in cache, fai '-!del>0' >  ")
    prefisso_cmd_msg = "msg "
    batch_file_path = "D:/Users/RedTy_ YT/Desktop/things/tools-per-dilettanti/windows/commandBats/msg.bat"

    # Carica le righe esistenti dal file batch
    if os.path.exists(batch_file_path) and os.path.getsize(batch_file_path) > 0:
        with open(batch_file_path, "r") as batch_file:
            lines = batch_file.readlines()
    else:
        lines = []

    # Numero totale di righe atteso nel file batch (incluso l'intestazione)
    total_lines = 6 if lines else 0

    if user_input.lower() == '-!del>0':
        # Elimina la riga dal file batch e esci dalla funzione
        if len(lines) >= 6:  # Assicurati che ci siano abbastanza righe nel file
            del lines[5]
            total_lines -= 1  # Aggiorna il numero totale di righe
            with open(batch_file_path, "w") as updated_batch_file:
                updated_batch_file.writelines(lines)
            print("Comando eliminato dalla cache.")
        else:
            print("Il file batch non ha abbastanza righe. Controlla il file.")
        return

    # Se l'input non è per eliminare la riga, inserisci il comando nel file batch
    if len(lines) >= total_lines:  # Assicurati che ci siano abbastanza righe nel file
        del lines[5]
        lines.insert(5, prefisso_cmd_msg + user_input + "\n")
        total_lines += 1  # Aggiorna il numero totale di righe
        with open(batch_file_path, "w") as updated_batch_file:
            updated_batch_file.writelines(lines)
        print("Comando aggiornato nella cache.")
    else:
        print("Il file batch non ha abbastanza righe. Controlla il file.")
    msgBat.esegui_file_batch(batch_file_path="D:/Users/RedTy_ YT/Desktop/things/tools-per-dilettanti/windows/commandBats/msg.bat")


def main():
    while True:
        user_input = input("Inserisci il comando da eseguire (o 'exit' per uscire): ")
        if user_input.lower() == 'exit':
            print("Sei sicuro di voler uscire? Gli output verranno salvati solo nel cmd.")
            user_input = input("Digita 'si' per uscire: ")
            if user_input.lower() == 'si':
                print("Chiusura...")
            elif user_input.lower() == 'no':
                continue
            break
        elif user_input.lower() == 'ipconfig':
            R1()
        elif user_input.lower() == 'help':
            R2()
        elif user_input.lower() == 'tools/settings/ipconfig/arpbat_path/info':
            R3()
        elif user_input.lower() == 'clearexit':
            print("Sei sicuro di voler uscire pulendo tutto il cmd?")
            user_input = input("Digita 'si' per uscire: ")
            if user_input.lower() == 'si':
                print("Chiusura ed eliminazione del cmd corrente...")
                subprocess.call("cls", shell=True)
            elif user_input.lower() == 'no':
                continue
            break
        elif user_input.lower() == 'clearexit -!def':
            print("Chiusura ed eliminazione del cmd corrente...")
            time.sleep(2)
            subprocess.call("cls", shell=True)
            break
        elif user_input.lower() == 'clear':
            print("Sei sicuro di voler eliminare tutta la cronologia cmd?")
            user_input = input("Digita 'si' per confermare: ")
            if user_input.lower() == 'si':
                print("Eliminazione del cmd corrente...")
                time.sleep(2)
                subprocess.call("cls", shell=True)
            elif user_input.lower() == 'no':
                continue
            else:
                print("Risposta errata. Prova a scrivere una risposta esistente come 'si' o 'no'")
        elif user_input.lower() == 'msg':
            R4()

        else:
            print("Comando errato. Prova a scrivere un comando esistente")

if __name__ == "__main__":
    main()
