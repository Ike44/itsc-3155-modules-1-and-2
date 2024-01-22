nums = []
even = []

text = input("Enter a number or QUIT to quit: ")
while(text != "QUIT"):
    nums.append(text)
    text = input("Enter a number or QUIT to quit: ")

for i in nums:
    if int(i) % 2  == 0:
        even.append(i)

print("All Nums: ", nums)
print("Even Nums: ", even)