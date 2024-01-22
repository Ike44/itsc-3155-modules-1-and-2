grade = int(input("Enter a grade from 0 to 100: "))

if grade < 100 and grade >=90:
    result = "A"
elif grade < 90 and grade >=80:
    result = "B"
elif grade < 80 and grade >=70:
    result = "C"
elif grade < 70 and grade >=60:
    result = "D"
elif grade < 60:
    result = "F"

print("Your result is", result)