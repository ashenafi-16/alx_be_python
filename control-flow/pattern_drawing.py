length = int(input("Enter the size of the pattern: "))
j = length
while j >= 0:
    for i in range(length):
        print('*', end="")
    j -= 1
    if j == 0:
        break
    print()
    