# #Write a script that takes in a string from the user. Print the string where all the lower case
# # letters are shifted to the front and the spaces removed. Keep the relative order of the lower case
# # letters and upper case letters.

text = input("Enter a string to be re-arranged: ")

lower = [char for char in text if char.islower()]
upper = [char for char in text if char.isupper()]

final = ''.join(lower) + ''.join(upper)

print(final)
