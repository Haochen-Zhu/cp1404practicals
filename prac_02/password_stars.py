"""change password to stars"""

# imports
password_len_min: int = 6


def main():
    """change password to stars"""
    password = get_password()
    password_len = get_password_length(password)
    while password_len < password_len_min:
        print("Password too short")
        password = get_password()
        password_len = get_password_length(password)

    print_stars(password_len)


def get_password():
    password = str(input(f"Type your password (not less than {password_len_min} characters): "))
    return password


def get_password_length(password):
    password_len = int(len(password))
    return password_len


def print_stars(password_len):
    for i in range(password_len):
        print("*", end='')


main()
