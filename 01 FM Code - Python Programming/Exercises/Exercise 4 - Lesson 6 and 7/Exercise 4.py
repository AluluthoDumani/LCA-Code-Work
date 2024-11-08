   # Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["apple","kiwi","naartjie"]
# TODO: Use a for loop to print each fruit in the list
for x in fruits:
    print(x)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
x = 5
while x>0:
    print(x)
    x-=1

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for x in range(1 ,11):
    print(x**2)
#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colour = ("red","grey","yellow","pink","nude")
# TODO: Use a for loop to select and print 3 random colors from the list
limit = 3
for x in colour[:3]:
    random_colour = random.choice(colour)
    print(random_colour)

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"  
"""

# TODO: Import the custom module and use its functions
import math_operations

# TODO: Use a while loop to create a simple calculator

import math_operations

print("icalculator")

def calculator():
    while true:
       operation = input("Please use any of the operations (+, -, *, /) or type 'exit' to quit: ")
       num_1 = float(input("enter number 1"))
       num_2 = float(input("enter number 2"))
     
       if operation == "exit" :
         print("exit")
       break
       
       elif operation == "+":
           answer = math_operations.add(num_1 ,  num_2)
           print(answer)
       
       elif operation == "-":
           answer = math_operation.subtract(num_1 , num_2)
       
       elif operation == "*" :
           answer = math.operation.multiply(num_1 , num_2)
           print(answer)
       
       elif operation == "/" :
           answer = math_operations.divide(num_1 , num_2)
           
       else:
           print("error try again")

calculator()
           


