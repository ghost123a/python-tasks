import string
import random

print("Welcome to HNG Tech")
print("Please set up your Log in Account")


def user_details():
    first_name = input("first name: ")
    last_name = input('last name: ')
    email = input("email: ")

    user_list = [first_name, last_name, email]
    return user_list


def create_password(user_list):
    N = 5
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k = N))
    new_password = str(user_list[0][0:2] + user_list[1][-2:] + random_string)
    return new_password


status = True

users = {}
user_no = 1

while status:

    user_list = user_details()

    new_password = create_password(user_list)
    print("your password is:" + new_password)
    print("do you like the password? yes or no")
    accept_password = input(": ")
    if accept_password == "yes":
        user_list.append(new_password)
        users[user_no] = user_list
    else:
        gen_password = input("create new password: ")
        while len(gen_password) < 7:
            gen_password = input("create new password not less than 7 characters: ")
        else:
            user_list.append(gen_password)
            users[user_no] = user_list

    new_user = input("would you like to enter a new user? yes or no: ")

    if new_user == "no":
        status = False
    for item in users:
        print(users.get(item))
        break

    else:
        status = True
        user_no = user_no + 1