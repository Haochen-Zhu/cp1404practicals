"""change password to stars"""

# imports
password_len_min: int = 6


def main():
    """change password to stars"""
    password = get_password()
    password_len = int(len(password))
    while password_len < password_len_min:
        print(password_len < password_len_min)
        print("Password too short")
        password = get_password()
        password_len = int(len(password))

    for i in range(password_len):
        print("*", end='')


def get_password():
    password = str(input(f"Type your password (not less than {password_len_min} characters): "))
    return password


main()
