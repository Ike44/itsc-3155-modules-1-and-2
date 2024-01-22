text1 = input("Enter the first string: ")
text2 = input("Enter the second string: ")

if text1.endswith(text2) or text2.endswith(text1):
    print("True")
else:
    print("False")