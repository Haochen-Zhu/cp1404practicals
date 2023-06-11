"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# (G)et a valid score (must be 0-100 inclusive)
# (P)rint result (copy or import your function to determine the result from score.py)
# (S)how stars (this should print as many stars as the score)
# (Q)uit

# display menu
# get choice
# while choice != <quit option>
#     if choice == <first option>
#         <do first task>
#     elif choice == <second option>
#         <do second task>
#     ...
#     elif choice == <n-th option>
#         <do n-th task>
#     else
#         display invalid input error message
#     display menu
#     get choice
# <do final thing, if needed>


def main():
    choice_01 = get_choice()
    while choice_01 != "Q":
        while choice_01 != "G":

            score = get_score()
            while score < 0 or score > 100:
                print("Invalid score")
                score = get_score()

            if choice_01 == "G":

                score = get_score()
                while score < 0 or score > 100:
                    print("Invalid score")
                    score = get_score()

            elif choice_01 == "P":
                print(grade_score(score))
            elif choice_01 == "S":
                print_stars(score)
                print("")
            else:
                print(f"Invalid input")
            choice_01 = get_choice()
        choice_01 = get_choice()

    print("Thanks for using.")


def get_choice():
    choice = str(str.upper(input("(G)et a valid score (must be 0-100 inclusive)\n"
                                 "(P)rint result (copy or import your function to determine the result from score.py)\n"
                                 "(S)how stars (this should print as many stars as the score)\n"
                                 "(Q)uit)\n>>>")))
    return choice


def get_score():
    score = float(input("Enter score: "))
    return score


def grade_score(a):
    if a > 100:
        return "Invalid score"
    elif a < 0:
        return "Invalid score"
    elif a > 90:
        return "Excellent"
    elif a >= 50:
        return "Passable"
    elif a < 50:
        return "Bad"


def print_stars(a):
    for i in range(int(a)):
        print("*", end='')


main()
