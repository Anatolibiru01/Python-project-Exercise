import random
coins = []
for i in range(100):
    probablities = random.choice(["H", "T"])
    coins.append(probablities)

lenght_of_H = []
for check in coins:
    if check == "H":
        lenght_of_H.append(1)

number_of_T = 100 - len(lenght_of_H)
number_of_H = len(lenght_of_H)

print(f"The number 0f H is: {number_of_H} The number of T isn: {number_of_T}")