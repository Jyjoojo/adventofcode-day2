from util_fonctions import *

def main():
    # Lecture des rapports depuis le fichier input.txt
    with open("input.txt", "r") as f:
        matrix = [list(map(int, line.strip().split())) for line in f if line.strip()]

    # Compteurs
    safe_without_dampener = 0
    safe_with_dampener = 0

    for row in matrix:
        if is_safe_with_dampener(row):
            if is_safe(row):
                safe_without_dampener += 1
            else:
                safe_with_dampener += 1

    print("Rapports sûrs sans le dampener :", safe_without_dampener)
    print("Rapports sûrs grâce au dampener :", safe_without_dampener + safe_with_dampener)
if __name__ == "__main__":
    main()
