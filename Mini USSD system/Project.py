import csv
import random
import string
import hashlib


def admin():  # to read the user info from csv file and register multiple users
    print("Verify Admin.")
    Ad_UN = input("User_Id: ").lower()  # admin
    Ad_Pas = input("Password: ").lower()  # admin
    if Ad_UN == "admin" and Ad_Pas == "admin":
        print("\nAdmin Page, Access only by admin!\n"
              "1. Deposit \n2. Search user.\n3. Register Multiple user at a time.")
        admin = input("   : ")
        if admin == "1":
            with open("text.csv", mode='r') as file:
                reader = list(csv.reader(file))

            user_id = input("User ID: ")

            for row in reader:
                if user_id == row[0]:
                    row[1] = int(row[1]) + int(input("Enter Cash amount: "))
                    update = True
                    break
                else:
                    print(f"{user_id} not found!")
                    update = False
                    break

            if update:
                with open("text.csv", mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(reader)
                print("   Cash Updated!\n")
                main_layer()
        elif admin == "2":
            search_user = input("Search user(by name): ").lower()
            data = []
            with open("file.csv", mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if search_user == row[0]:
                        data.append(row)
            if data:
                print(f"\nThere is {len(data)} people match with name: {search_user.upper()}\n"
                      "Name                     User_id              Encoded Password")
                for match in data:
                    if search_user == match[0]:  # print each row of user infos
                        print(
                            f"{match[0]} {" "*(23-len(match[0]))} {match[1]} {" "*(20-len(match[1]))}{match[-1]}")
            else:
                print(f"There is no {search_user} in the database.")

        elif admin == "3":
            num = int(input("Enter number of user: "))
            for i in range(num):
                print(f"Enter Information of user ({i+1})")
                registration()
            main_layer()
        else:
            print("Invalid!")
    else:
        main_layer()


def user():  # login and new user registeration layer
    print("Hello user, welcome! \n1. Login  \n2. Register(new) \n3. Back")
    user = input("      : ")
    if user == "1":
        login()
    elif user == "2":
        registration()
    elif user == "3":
        main_layer()
    else:
        print("Invalid option!")


def encode_password(password):  # to encrypt pass
    return str(hashlib.md5(password.encode()).digest())


def login():
    user_id = input("User_id: ")
    with open("file.csv", mode='r') as file:
        reader = list(csv.reader(file))

    user = next((row for row in reader if row[1] == user_id), None)

    if user:
        password = input("Password: ")
        encode_pass = encode_password(password)
        for _ in range(3):
            if encode_pass == user[-1]:
                return Services(user[0], user_id)
            password = input("Incorrect password. Try again: ")
            encode_pass = encode_password(password)
        print("You tried 3 times. Check your credentials and try again later.\n")
    else:
        print(f"No such user_id: {user_id}\n")
        main_layer()


def registration():
    def user_id_check():  # to check whether the user id is used or not
        users = []
        user = input("  Enter user_id(e.g: user123): ")
        with open("file.csv", mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                users.append(row[1])

            while users:
                if user not in users:
                    return user
                else:
                    user = input("This user_id is taken. Try other user id: ")
                    continue
    register = []

    def user_info(register):  # to save registration info on csv file
        with open("file.csv", mode='a', newline='') as file:
            writer = csv.writer(file)  # write the last registered user info
            writer.writerow(register[-1])

    print("Fill the following correctly!")
    name = input("  Full name: ").lower()
    new_user_id = user_id_check()
    while True:
        try:
            password = int(input("  Enter password(only 4 digit): "))
            if len(str(password)) == 4:
                break
            else:
                print("    Invalid!, try again (e.g: 1234)\n")
                pass
        except ValueError:
            print("      Don't use letters only 4 digits(e.g: 1234)!\n")
            pass

    register.append((name, new_user_id, encode_password(str(password))))
    user_info(register)  # to save the registration info
    with open("text.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow((new_user_id, 50))
    print(
        f"\nsuccessfully registred! Your Username and password is registred\n")
    user()


def change_password(user_id):

    def is_pass_valid():  # to take password and check value error
        while True:
            try:
                password = int(
                    input("Enter new password(only 4 digit): "))
                if len(str(password)) == 4:
                    return encode_password(str(password))  # to encode password
                else:
                    print("    Invalid!, try again (e.g: 1234)\n")
                    pass
            except ValueError:
                print("    Don't use letters only 4 digits(e.g: 1234)!\n")
                pass

    def otp_and_pass():  # to check otp and return the is_pass_valid
        ran = str("".join(random.choices(string.digits, k=4)))
        print(f"Don't Share this one time password(OTP):-> {ran}")
        otp = input("Enter OTP: ")
        if otp == ran:  # to check otp and ask password
            return is_pass_valid()
        else:
            print("Incorrect otp!")

    with open("file.csv", mode='r') as file:
        reader = list(csv.reader(file))

    password = encode_password(input("Current password: "))

    for row in reader:
        updated = password == row[2]
        if user_id == row[1]:
            if updated:
                row[2] = otp_and_pass()
                break

    if updated:
        with open("file.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)
        print("Password Updated!")
        main_layer()
    else:
        print(f"Incorrect old password!")


def Services(name, user_id):  # the main app of the system after logged in
    print(f"\nWelcome {name.upper()}.")

    print("0. Change password.\n1. Balance.\n2. Transfer money.\n"
          "3. Air time.\n4. About.\n5. logout")
    select = int(input("   : "))

    with open("text.csv", mode='r') as file:
        reader = list(csv.reader(file))

    if select == 0:
        change_password(user_id)
    elif select == 1:
        for row in reader:
            if user_id == row[0]:
                print(f"Your Balance is: {row[1]}")
    elif select == 2:
        print("Not opened yet!")
    elif select == 3:
        phone = input("Enter phone number: ")
        air_time = int(input("Enter Amount: "))
        for row in reader:
            if user_id == row[0]:
                row[1] = int(row[1]) - air_time
                update = True
                break
        if update:
            with open("text.csv", mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(reader)
        print(
            f"  You are succesfully buy {air_time} birr airtime\n  For phone number: {phone}")
    elif select == 4:
        print("X bank mobile transaction ussd system")
    elif select == 5:
        exit
    else:
        print("Invalid")


def main_layer():  # admin and user identifer
    print("\nwelcome, Select.")
    print("1. Admin\n2. User\n3. Exit")
    first = input("   : ")
    num = ("1", "2", "3")
    if first in num:
        if first == "1":
            admin()
        elif first == "2":
            user()
        else:
            print("logged out!!")
            # exit
    else:
        print("Invalid value, Tyr again!\n ")


if __name__ == "__main__":
    main_layer()
