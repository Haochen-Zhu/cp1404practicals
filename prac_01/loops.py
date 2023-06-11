# example.
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
n = int(input("number of stars:"))
for i in range(1, n+1, 1):
    print("*", end='')
print()

# d.
n = int(input("number of rows:"))
for i in range(n+1):
    for j in range(i):
        print("*", end='')
    print()
