list1 = []
list2 = []
list3 = []

for i in range(5):
    list1.append(int(input("Enter a number for the first list: ")))

for i in range(5):
    list2.append(int(input("Enter a number for the second list: ")))

dupes = set(list1) & set(list2)
for x in dupes:
    list3.append(x)

print("First list: ", list1)
print("Second List: ", list2)
print("Common List: ", list3)