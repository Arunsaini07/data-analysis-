FILE_NAME = "password.txt"


def save_password(website, password):
    with open(FILE_NAME, "a") as f:
        f.write(f"{website} - {password}\n")

    print("Password saved successfully!")


def get_password(website):

    try:
        with open(FILE_NAME, "r") as f:

            for line in f:
                if website in line:
                    print("Password:", line.strip())
                    return

            print("No password found.")

    except FileNotFoundError:
        print("No passwords saved yet.")


def main():

    while True:

        print("\n1. Save password")
        print("2. Get password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            website = input("Enter website name: ")
            password = input("Enter password: ")

            save_password(
                website,
                password
            )

        elif choice == "2":

            website = input(
                "Enter website name: "
            )

            get_password(website)

        elif choice == "3":

            print("Exiting...")
            break

        else:
            print("Invalid choice")


main()