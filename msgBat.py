import subprocess

def esegui_file_batch(batch_file_path):
    try:
        subprocess.run([batch_file_path], shell=True, check=True)
        print("File batch eseguito con successo.")
    except subprocess.CalledProcessError as e:
        print("Si è verificato un errore durante l'esecuzione del file batch:", e)


if __name__ == "__main__":
    esegui_file_batch()