# ---------------- Problem #01 – Debugging ----------------
# Concept: String Manipulation, Concatenation, and Debugging Errors
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')



# ---------------- Problem #02 – Inputs ----------------
# Concept: input() always returns a string, len() finds length
my_name = input("Please Enter your name: ")
name_length = len(my_name)
print(name_length)




# ---------------- Problem #03 – Variables (Swapping) ----------------
# Concept: Variable swapping using a temporary variable
a = input("enter any value:  ")
b = input("What is temperature outside: ")

temp = a
a = b
b = temp

print("a: " + a)  # "a: " is a string label, + joins string + variable
print("b: " + b)





# ---------------- Problem #04 – Printing to the Console ----------------
# Concept: print() function in Python
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")




# ---------------- Problem #05 – Data Types ----------------
# Concept: input() returns string, subscripting [] picks characters, int() converts
two_digit_number = input("Type a two-digit number: ")
print(type(two_digit_number))  # always string

first_digit = int(two_digit_number[0])  # pick first digit
second_digit = int(two_digit_number[1]) # pick second digit
print(first_digit + second_digit)       # add integers





# ---------------- Problem #06 – Your Life in Weeks ----------------
# Concept: f-strings, formatting, calculations
user_age = input("What is your current age?: " )
age = int(user_age)

max_age = 90
years_left = max_age - age

days = years_left * 365
weeks = years_left * 52
months = years_left * 12

message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)





# ---------------- Problem #07 – Odd or Even ----------------
# Concept: Modulus (%) operator checks remainder
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")




# ---------------- Problem #08 – BMI Calculator 2.0 ----------------
# Concept: if/elif, round(), ANSI escape codes for bold
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

BMI = round(weight / height**2)

if BMI <= 18.5:
    print(f"Your BMI is {BMI}, you are \033[1munderweight\033[0m.")
elif BMI > 18.5 and BMI < 25:
    print(f"Your BMI is {BMI}, you have a \033[1mnormal weight\033[0m.")
elif BMI > 25 and BMI < 30:
    print(f"Your BMI is {BMI}, you are \033[1mslightly overweight\033[0m.")
elif BMI > 30 and BMI < 35:
    print(f"Your BMI is {BMI}, you are \033[1mobese\033[0m.")
elif BMI > 35:
    print(f"Your BMI is {BMI}, you are \033[1mclinically obese\033[0m.")





# ---------------- Problem #09 – Leap Year ----------------
# Concept: Nested if and combined condition using logical operators
year = int(input('Enter year to check leap year: ')) 
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap year.")
else:
    print("Not leap year.")






# ---------------- Problem #10 – Pizza Order Program ----------------
# Concept: if/elif, dictionary, [] lookup operator, .strip(), .upper()
size = input("Choose a size (S, M, L): ").strip().upper()
add_pepperoni = input("Add pepperoni? (Y/N): ").strip().upper()
extra_cheese = input("Extra cheese? (Y/N): ").strip().upper()

base_prices = {"S": 15, "M": 20, "L": 25}
pepperoni_prices = {"S": 2, "M": 3, "L": 3}

bill = base_prices[size]   # dictionary lookup using []
if add_pepperoni == "Y":
    bill += pepperoni_prices[size]
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")





# ---------------- Problem #11 – Love Calculator ----------------
# Concept: count(), concatenation vs addition, string methods
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
combined_names = (name1 + name2).lower()

t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
true_score = t + r + u + e

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")
love_score = l + o + v + e

final_score = int(str(true_score) + str(love_score))  # concatenation not addition

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif 40 <= final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")




# ---------------- Problem #12 – Treasure Island ----------------
# Concept: Nested if-else, input().lower(), \n newline character
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'.\n").lower()
if choice1 == "left":
    choice2 = input("You've come to a lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors: red, yellow, and blue. Which colour do you choose?\n").lower()
        if choice3 == "yellow":
            print("You found the treasure! 🏆 You Win!")
        elif choice3 == "red":
            print("It's a room full of fire 🔥. Game Over.")
        elif choice3 == "blue":
            print("You enter a room of beasts 🐉. Game Over.")
        else:
            print("You chose a door that doesn't exist. 🚪 Game Over.")
    else:
        print("You get attacked by an angry trout 🐟. Game Over.")
else:
    print("You fell into a hole 🕳️. Game Over.")
