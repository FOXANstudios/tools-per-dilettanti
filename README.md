# Custom CMD
 Dei tool standard per chi vuole cominciare con l'Informatica.

 > [!WARNING]
 > Per ora questo progetto è disponibile **solo per Windows 7/8/10/11**.

# Come si usano?

> [!WARNING]
> I comandi sono ancora in fase di sviluppo.

<details>
<summary>Clicca per espandere il menu</summary>

- [exit](#exit)
- [ipconfig](#ipconfig)
- [help](#help)
- [clearexit](#clearexit)
  | -!def

- [clear](#clear)
- [msg](#msg)

</details>

# Come si installa?

> [!WARNING]
> Il programma è ancora in fase di sviluppo, ma è scaricabile.

Il Custom CMD può essere facilmente installato da una riga di codice:
```
git clone https://github.com/FOXANstudios/tools-per-dilettanti
```
Questo custom cmd è stato creato da @redtyyt per alcune lezioni di informatica a persone dilettanti in quest'ultima. Può però anche essere installata da un utente **non registrato alle lezioni private**.
#
# exit

- **Scopo**: Il comando 'exit' fa uscire l'utente corrente dal CMD. (Il cmd viene terminato).

- **Opzioni**: Non ha nessuna opzione, ma ha 2 scelte interne: 'si' e 'no'.


#
# ipconfig

- **Scopo**: Il comando 'ipconfig' mostra le informazioni di rete dell'utente (solo su Windows).

- **Opzioni**: Non ha nessuna opzione.

- **Response**: La response viene salvata nel file "responseArp.env"

#
# help

- **Scopo**: Il comando 'help' mostra una lista di tutti i comandi disponibili.

- **Opzioni**: Non ha nessuna opzione.

#
# clearexit

- **Scopo**: Il comando 'clearexit' unisce la funzione cls e exit, così da cancellare e allo stesso tempo uscire dal terminale.

- **Opzioni**: *-!def* = **Non mostrare il messaggio di conferma**.

#
# clear

- **Scopo**: Il comando 'clear' chiama il subprocess "cls", cioè pulisce tutto il terminale.

- **Opzioni**: Non ha opzioni.

#
# msg

- **Scopo**: Il comando 'msg' usa un comando Windows in un file bat che manda un messaggio a l'ip, utente selezionato.

- **Opzioni**: ricevitore = *, {ip}, {nome_pc}; messaggio = {messaggio}

- **Response**: La response non viene conservata ma viene mostrata sottoforma di finestra msg standard.
