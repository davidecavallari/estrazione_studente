import random

# Nome del file da cui leggere l'elenco dei nomi
file_nomi = "nomi.txt"

try:
    with open(file_nomi, 'r') as file:
        nomi = file.readlines()
        
    # Rimuovi gli eventuali spazi bianchi (come i caratteri di newline) da ciascun nome
    nomi = [nome.strip() for nome in nomi]
    
    # Estrai a sorte uno dei nomi
    nome_estratto = random.choice(nomi)
    
    print("Nome estratto:", nome_estratto)
except FileNotFoundError:
    print(f"Il file {file_nomi} non è stato trovato.")
except Exception as e:
    print(f"Si è verificato un errore: {e}")
