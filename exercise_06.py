row = int(input("Enter a row num from 1 to 5: "))
column = int(input("Enter a column num from 1 to 5: "))

for i in range(1, 6):
    for x in range(1, 6):
        if (i == row and x == column):
            print(1, end= " ")
        else:
            print(0, end= " ")
    print()