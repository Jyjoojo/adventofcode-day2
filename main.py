from util_fonctions import *
def main():
    # Lecture des rapports depuis le fichier input.txt
    with open("input.txt", "r") as f:
        matrix = [list(map(int, line.strip().split())) for line in f if line.strip()]

    # Comptage des rapports sûrs
    compteur = 0
    for row in matrix:
        if is_safe(row):
            compteur += 1

    print("Nombre de rapports sûrs :", compteur)

if __name__ == "__main__":
    main()