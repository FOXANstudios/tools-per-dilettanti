import sys
from dotenv import load_dotenv
import subprocess

load_dotenv()

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

