list1 = []
once = []

for i in range(1, 11):
    num = input("Enter number " + str(i) + ": ")
    list1.append(num)

for x in list1:
    if list1.count(x) == 1:
        once.append(x)

print("Original List: ", list1)
print("Nums that appear once: ", once)