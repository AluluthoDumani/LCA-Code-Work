# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x = 0
x +=3
# TODO: Multiply y by 2 using the *= operator
y = 1
y *= 2

# TODO: Divide x by y and store the result in a variable called 'result'
result = x/y
# TODO: Print the value of 'result'
print(result)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a = 13
b = 10
if a > b:
   print(a>b)
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
b = 10
if b %2 == 0:
    print("even")
else :
    print("odd")
# TODO: Create a condition that checks if c is less than or equal to a
a=13
c=6
print(c<a)
#  TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_condition = a>b or (b%2 ==0 and c<=a)
# TODO: Print the value of 'final_condition'
print(final_condition)
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = int(input("please insert your test score between 0-100:"))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if score >= 90 :
    print("A ")
elif score >= 89: 
    print("B") 
elif score >= 79:
    print("C")
elif score >= 69:
    print("D")  
else:
    print("Failed dismally")

# TODO: Print the grade for the given score
print(score)
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = int(input("please insert any number"))
num2 = int(input("please insert any number"))

# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("please use any of the operations, (/ ,* , - , + ): " )
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
if operation == "+":
    results = num1 + num2
elif operation == "-":
    results = num1-num2
elif operation == "*" :
     results = num1*num2
if operation == "/" and num2 == 0:
    print ("not allowed")

elif operation == "/":
    results = num1/num2 



# TODO: Handle the case of division by zero


# TODO: Print the result of the operation
print(results)