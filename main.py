from  db_connections import check_user


if __name__ == "__main__":
    name = input("Enter name ")
    password = input("Enter Password ")

    if check_user(name, password):
        print("user exists")