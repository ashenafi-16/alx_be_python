length = int(input("Enter the size of the pattern: "))
while length > 0:
    for i in range(4):
        print('*', end="")
    length-=1
    print()