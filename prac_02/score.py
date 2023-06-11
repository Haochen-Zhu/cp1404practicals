"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

import random


def main():
    score_01 = get_score()
    print(grade_score(score_01))

    score_02 = round(random.uniform(-10, 110), 2)
    print(f"random score: {score_02}")
    print(grade_score(score_02))


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


def get_score():
    score = float(input("Enter score: "))
    return score


main()
