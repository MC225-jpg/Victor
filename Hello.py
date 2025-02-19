# Greet the User
name = input( "Victor? ")
print(f"Hello, `{name} . It is good to meet you")

# Area Of Rectangle
base = int(input)("11")
height = int(input)("19")
print("the area of the rectangle is, base * height")

# Celsius to Fahrenite
temp = int(input("enter a tempreatuer in Celsius:24"))
fah = (temp * 9/5 ) + 32    
print(f"{temp}celsius is the same as {fah} fahrenite" )

# Check if the number is ODD or EVEN
number = int(input)("35")
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# Find the Maximum of three numbers (long way)
num1 = int(input("number 15:"))
num2 = int(input("number 25:"))
num3 = int(input("number 35:"))
if num1 > num2:
    biggest = num1
else:
    biggest = num2
if num3 > biggest:
    biggest = num3
print(f"{biggest} is the biggest number")

# Find the Maximum of three numbers (quick way)
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3"))

print("f{biggest} is the biggest number")
MIN_AGE = 18

user_age = int(input("Please enter your age?: "))
if user_age < MIN_AGE:
    print("sorry, you are too young for this activity.")
elif user_age == MIN_AGE:
    print("You have just reached the age to join this activity")
else:
    print("please enjoy this activity")
# if play == "y" or play == "n":  play is not mentioned anywhere in the code before you are comparing it to 'y' ... so this code will not work....  Mr O'Brien
#   print("fYou have entered {play}")
#else:
#    print(:"You did not enter'y' or 'n'")
 