import arpWireless
import time
from dotenv import load_dotenv
import subprocess
import os

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
    Aiuto per il comando 'help':
    help -{comando} --> puoi digitare il comando 'help -{comando}' per avere informazioni sul comando richiesto.
    —————————————————————————————————————————————————————————————————————————————————————————————————————

    Aiuto per il comando 'ipconfig':
    help -ipconfig --> puoi digitare il comando 'help -ipconfig' per avere informazioni sul comando.
    """)


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
        else:
            print("Comando non eseguito correttamente")

if __name__ == "__main__":
    main()
