"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subj_data = get_data()
    print(subj_data)
    display_subjects(subj_data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        print(line)
        print(repr(line))
        line = line.strip()
        parts = line.split(',')
        print(parts)
        parts[2] = int(parts[2])
        print(parts)
        print("----------")
    input_file.close()


def display_subjects(subj_data):
    for subject in subj_data:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")


main()
