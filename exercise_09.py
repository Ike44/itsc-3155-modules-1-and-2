words = []
final = ""

for i in range(5):
    text = input("Enter a word: ")
    words.append(text)
    final = final + " " + text

print("Words: ", words)
print("One String:" + final)