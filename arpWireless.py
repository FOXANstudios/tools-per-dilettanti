import sys
import subprocess

def run_batch_file(batch_file_path):
    try:
        subprocess.run([batch_file_path], shell=True, check=True)
        print("File batch eseguito con successo.")
    except subprocess.CalledProcessError as e:
        print("Si è verificato un errore durante l'esecuzione del file batch:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <batch_file_path>")
        sys.exit(1)

    batch_file_path = sys.argv[1]
    run_batch_file(batch_file_path)
