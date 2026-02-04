import random
# # dice
try:
    dice = int(input("Set custom side of dice: "))
    print(F"Result: {random.randint(1, dice)}")
    print(" Do want try again or exit? \n1. Roll again \n2. Exit")

    while True:
        reputetion = input("Roll again(1) or exit(2): ")
        if reputetion == "1":
            print(F"Result: {random.randint(1, dice)}")
        elif reputetion == "2":
            break
        else:
            print("invalid choice")
            pass
except ValueError:
    print("invalid input!!")