import random

while True:
    game_choice = input("Rock, paper or scisser? (r/p/s): ").lower()
    dicts = {"r": "rock", "p": "paper", "s": "scisser"}
    choices = random.choice(["rock", "paper", "scissor"])

    if game_choice in dicts:
        print(f"You chose: {dicts[game_choice]} \nComputer chose: {choices}")
        if choices == dicts[game_choice]:
            print("you win")
            break
        else:
            print("you lose")
    else:
        print("Invalid choice!")
        continue

    cont = input("continue? (y/n): ").lower()
    if cont == "y":
        continue
    else:
        break
