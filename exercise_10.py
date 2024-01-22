text = input("Enter a string: ")

characters = list(text)
result = [characters[i:i+3] for i in range(0, len(characters), 3)]

print(result)
