count = int(input("Enter a number(count): "))

list1 = []
for i in range(count):
    list1.append(float(input("Enter number " + str(i) + ": ")))

print("List:",list1)
print("Average:", (sum(list1)/len(list1)))