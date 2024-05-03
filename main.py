import subprocess

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Eseguito comando: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione del comando '{command}': {e}")

def main():
    while True:
        user_input = input("Inserisci il comando da eseguire (o 'exit' per uscire): ")
        if user_input.lower() == 'exit':
            break
        execute_command(user_input)

if __name__ == "__main__":
    main()