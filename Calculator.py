


ClassGrades = {}

while (True):
    print("\n")

    category = input("Enter category name or input '0' to stop!\n\n")

    if (category == '0'):
        break

    Value = []

    Percentage = round(float((input("Enter the grade percentage of the category.\n"))), 2)
    print("\n")
    Grade = round(float(input("Enter the grade for the category.\n")), 2)
    print("\n")

    Value.append(Percentage)
    Value.append(Grade)

    try:
        ClassGrades[category] = Value

    except KeyError as e:
        print("This category already exists!\nPlease try again!\n\n")
        continue

    else:
        x = input("Would you like to confirm the data inputted?\n1: Confirm\n0: Change\n")

        if (x == '0'):
            ClassGrades.popitem()
            continue
            
        else:
            print("Category submitted!")
            print("\n\n")


total = 0

for key, value in ClassGrades.items():
    total += (value[0] * value[1])

print(f"Your total grade is {round((total/100),2)}%")