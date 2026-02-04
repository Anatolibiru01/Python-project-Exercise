import random

colors = ["orange", "yellow", "green", "blue", "purple", "red", "indigo"]

random = random.choices(colors, k=3)

sequence = ["first", "second", "third"]
# print(random)
while True:
    try:
        guesses = []
        fre = []
        for i in range(3):
            guess = input(f"Guess a {sequence[i]} color: ")
            guesses.append(guess.lower())

            if guesses[i] == random[i]:
                fre.append(1)
            else:
                fre.append(0)
        # //// display section
        if sum(fre) == 3:
            print("\n  You guessed right order!\n")
            break
        else:
            print(f"  You guessed {sum(fre)} correct guesses\n")
            pass
    except ValueError:
        print("Incorrect input try again!\n")
