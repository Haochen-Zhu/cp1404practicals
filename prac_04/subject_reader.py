"""
CP1404 Practical
Data file -> lists program
"""

"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data: list = []
    for line in input_file:
        print(line, sep="")  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")

        data.append(parts)

    input_file.close()
    return data


# def display_data():
#     input_file = open(FILENAME)
#     for line in input_file:
#         line = line.strip()  # Remove the \n
#         parts = line.split(',')  # Separate the data into its parts
#         print(f"{parts[0]} is taught by {parts[1]} and has {parts[2]} students")
#     input_file.close()


def display_data(a):
    for i in range(len(a)):
        print(f"{a[i][0]} is taught by {a[i][1]} and has {a[i][2]} students")




main()
