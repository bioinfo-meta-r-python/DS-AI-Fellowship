# Flowchart-01

height = int(input("Enter your height: "))
if height > 120:
    print('Can ride')
else:
    print("Can't ride")


# Flowchart-02

height = int(input("Enter your height: "))

if height > 120:
    print('Can ride')
    age = int(input("Enter your age: "))
    if age <= 18:
        print('$7')
    elif age > 18:
        print('$12')
else:
    print("Can't ride")



# Flowchart-03

height = int(input("Enter your height: "))

if height > 120:
    print("Can ride")
    age = int(input("Enter your age: "))
    bill = 0

    if age < 12:
        bill += 5
        print("+$5")
    elif 12 <= age <= 18:
        bill += 7
        print("+$7")
    else:  # age >= 18
        bill += 12
        print("+$12")

    photo = input("Want a photo? yes/no: ")
    if photo == "yes":
        bill += 3
        print("+$3")

    print(f"The total bill is ${bill}")
else:
    print("Can't ride")



# Flowchart-04

height = int(input("Enter your height: "))

if height > 120:
    print("Can ride")
    age = int(input("Enter your age: "))
    bill = 0

    if age < 12:
        bill += 5
        print("+$5")
    elif 12 <= age < 18:
        bill += 7
        print("+$7")
    elif 45 <= age <= 55:
        bill += 0
        print("+$0 (Free ride for 45–55)")
    else:  # age >= 18 but not 45–55
        bill += 12
        print("+$12")

    photo = input("Want a photo? yes/no: ")
    if photo == "yes":
        bill += 3
        print("+$3")

    print(f"The total bill is ${bill}")
else:
    print("Can't ride")
