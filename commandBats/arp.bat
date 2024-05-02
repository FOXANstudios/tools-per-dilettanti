@echo off

REM Esegui il comando ipconfig e salva la risposta solo se non è vuota
ipconfig > responseArp.tmp

REM Controlla se il file temporaneo contiene dei dati
for %%I in (responseArp.tmp) do set FileSize=%%~zI

REM Se il file temporaneo non è vuoto, copia il suo contenuto in responseArp.env
if %FileSize% GTR 0 (
    copy /Y responseArp.tmp responseArp.env > nul
    del responseArp.tmp > nul
    echo "Comando IPCONFIG eseguito e salvato in responseArp.env"
    timeout /t 2 > nul
    echo "Attendi... Apertura in corso del file responseArp.env"
    echo "Ti raccomando di scegliere un'app come Blocco Note"
    timeout /t 5 > nul
    responseArp.env
) else (
    del responseArp.tmp > nul
    echo "Comando IPCONFIG non ha restituito alcun output. Il response non è stato registrato."
)

REM Etichetta di pulizia per eliminare il file temporaneo
:cleanup

REM Elimina il file temporaneo se esiste
if exist responseArp.tmp del responseArp.tmp
