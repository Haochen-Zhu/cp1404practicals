out_file = open("name.txt", "w")
name = input("Type your name here: ")
out_file.write(name)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

in_file = open("numbers.txt", "r")
for line in in_file:
    print(line)
in_file.close()
