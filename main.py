import random
while True:
    while True:
        vstup = input("Zadej rock/paper/scisors/end: ")
        if vstup not in ["rock", "paper", "scisors", "end"]:
            print("Špatný vstup")
        else:
            break
    vysledek = random.choice(["rock", "paper", "scisors"])
    print("Počítač zvolil:", vysledek)
    if vstup == vysledek:
        print("Remíza")
    elif vstup == "rock" and vysledek == "scisors":
        print("Vyhrál jsi")
    elif vstup == "paper" and vysledek == "rock":
        print("Vyhrál jsi")
    elif vstup == "scisors" and vysledek == "paper":
        print("Vyhrál jsi")
    elif vstup == "end":
        break
    else:
        print("Prohrál jsi")
