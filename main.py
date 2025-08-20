# Assignment 1 – Section B
# Write your answers below each question

# Q11: Swap variables
# Your code here

# Swap using a temporary variable
a = 10
b = 20

print("Before swapping: a =", a, "b =", b)
temp = a   
a = b      
b = temp   
print("After swapping: a =", a, "b =", b)

# Swap without using a temporary variable
x = 5
y = 15

print("Before swapping: x =", x, "y =", y)

x, y = y, x   # Pythonic way of swapping

print("After swapping: x =", x, "y =", y)


# Q12: Number pattern
# Your code here

# Display a 6x6 square using the number 6

for i in range(6):
    for j in range(6):
        print(6, end=" ")
    print()                


# Q13: Factorial OR Password System
# Your code here

#Part A
# Program to calculate factorial of a number using a loop


num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial of", num, "is:", fact)

# Part B
# Program to simulate a simple password system

correct_password = "admin123"
attempts = 3

for i in range(attempts):
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access Granted")
        break
    else:
        print("Incorrect password. Attempts left:", attempts - i - 1)
else:
    print("Access Denied")
