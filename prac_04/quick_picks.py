"""
CP1404 program -- quick_pick
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("number of quick picks? "))
    while number_of_quick_picks < 0:
        print("wrong input")
        number_of_quick_picks = int(input("number of quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()
