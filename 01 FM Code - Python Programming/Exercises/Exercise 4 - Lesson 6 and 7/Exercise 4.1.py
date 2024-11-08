#------------------------------------------------------------------------------------
#Task 1: Function with Loop and Conditional Logic

# TODO: Define a function called 'check_attendance' that takes a list of names (students) and a list of absentees.
#       It should return a list of names of students who are absent.
def check_attendance(students_name , absentees):
    return absentees
students_name = ["Alice", "Bob", "Charlie", "David"]
absentees = ["Bob", "David"]

# TODO: Call 'check_attendance' with a list of ["Alice", "Bob", "Charlie", "David"] 
#       and a list of absentees ["Bob", "David"], and print the result.
absentees_list = check_attendance(students_name ,absentees)
print(absentees_list)

#------------------------------------------------------------------------------------
# Task 2: Function for Real-Life Data Processing

# TODO: Define a function called 'calculate_average_grade' that takes a dictionary where the keys are student names 
#       and the values are their grades, and returns the average grade of the class.
def calculate_average_grade(average_dict):
    average_dict = {"Alice": 85,
                "Bob": 92,
                "Charlie": 78,
                "David": 90
                }
    class_average = sum(average_dict.values()) / len(average_dict)
    return class_average


# TODO: Call the 'calculate_average_grade' function with the following dictionary:
#       {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}, and print the result.
average = calculate_average_grade(average_dict = {"Alice": 85,
                "Bob": 92,
                "Charlie": 78,
                "David": 90
                })
print(average)

#------------------------------------------------------------------------------------
# Task 3: Function Returning a Function (Higher-Order Function)

# TODO: Define a function called 'operation_selector' that takes a string "add" or "multiply" as a parameter,
#       and returns a function that either adds or multiplies two numbers.
def operation_selector(add , multiply):
    return add, multiply
operation = input("Select operation (+ or *): ")
    if operation == "+":
    
    else:
    print("try again")
    if operation == "*":
    return multiply
    else:
    print("try again")
# TODO: Use 'operation_selector' to get the "add" function, and then call it to add 4 and 6.
operator_selector = add
num_1 = int(input(insert number))
num_2 = int(input(insert number))

operator_selector = add(num_1 ,num_2)
print(operation_selector)
# TODO: Use 'operation_selector' to get the "multiply" function, and then call it to multiply 3 and 7.
operator_selector = multiply
num_1 = int(input(insert number))
num_2 = int(input(insert number))

operator_selector = multiply(num_1 ,num_2)
print(operation_selector)
#------------------------------------------------------------------------------------
# Task 4: Function for a Practical Scenario

# TODO: Define a function called 'calculate_trip_cost' that takes three parameters:
# • distance (in km), fuel_efficiency (km per liter), fuel_price (price per liter),
# • and returns the total cost of fuel for the trip.
def calculate_trip_cost(distance , fuel_efficiency , fuel_price):
    distance = float(input("distance_km:"))
    fuel_efficiency = float(input("fuel per litre:"))
    fuel_price = float(input("litres:"))
    return total_cost(distance*fuel_efficiency*fuel_price)


# Task : Using a for loop with a dictionary (Real-life Scenario: Grocery Shopping List)

# TODO: Create a dictionary with grocery items as keys and their quantities in stock as values.
grocery_inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Tomatoes": 25,
    "Bread": 15,
    "Milk": 10
}


# TODO: Use a for loop to print each item and its quantity in stock.

for key, value in grocery_inventory():
    print(key,value)

# TODO: Calculate and print the total number of items in stock (sum of all values in the dictionary).
total_items = sum(stock.values())
print(f'Total number of items in stock: {total_items}')

#------------------------------------------------------------------------------------
# Task 5: Using a while loop for banking (Real-life Scenario: ATM Pin Retry System)

# TODO: Ask the user to input their PIN.
# TODO: If the PIN is incorrect, ask the user to try again, but only allow 3 attempts.
# TODO: After 3 incorrect attempts, print "Account Locked". If the PIN is correct, print "Access Granted".

correct_pin = "1234"
attempts = 0
limit = 3

# TODO: Use a while loop to implement the retry system.
while attempts < limit:
    user_pin = input("Please enter your PIN: ")
    if user_pin == correct_pin:
        print("Access Granted")
        break  # Exit the loop if the PIN is correct
    else:
        attempts += 1
        print(f"Incorrect PIN. You have {max_attempts - attempts} attempt(s) left.")
    if attempts == max_attempts:
    print("Account Locked")    

#------------------------------------------------------------------------------------
# Task 6: Using a for loop with range() for a School Grading System

# TODO: Create a list with 10 random assignment scores (between 0 and 100).
score = [50,21,45,14,54,85,88,88,90,85,]
# TODO: Use a for loop to calculate the total score.
for x in score:
tot.score = sum(score)
    print(tot.score)
# TODO: Calculate and print the average score for the class.
average_score = tot.score / len(score)
# Bonus: Use conditional logic to print a congratulatory message if the average is above 75.
if average_score > 75:
    print("Great Job! Yall Passed")
import random

# List of 10 student scores.
scores = [random.randint(0, 100) for _ in range(10)]

# TODO: Calculate total and average scores.
x = tot.score + average_score
print(x)


#------------------------------------------------------------------------------------
# Task 7: Using the random module (Real-life Scenario: Random Team Selection)

# TODO: Create a list with the names of 20 participants.
# TODO: Use the random module to select 5 random participants.
# TODO: Print the names of the selected team members.

import random

# List of participants.
participants = [Swae,bob,beyonce,usher,riri,kanye ,tisha ,khwezi, mnisi,lizo,sive,mbali,mama,yaya,wewe,akum,ave,mvivi, west, zola,]

# TODO: Randomly select 5 people from the participants list.
limit = 5

for random_participants in participants [:5]:
    random_parts = random.choice(participants)
    print(random_parts)

#------------------------------------------------------------------------------------
# Task 8: Custom module for a Fitness Tracker (Real-life Scenario: Tracking Calories Burned)

# Step 1: Create a module named 'fitness_tracker.py' with the following functions:
"""
def walk_calories(distance_km):
    # Calories burned per km walking: 50
    return distance_km * 50

def run_calories(distance_km):
    # Calories burned per km running: 100
    return distance_km * 100

def cycle_calories(distance_km):
    # Calories burned per km cycling: 70
    return distance_km * 70
"""

# Step 9: Use the custom module in your main script:
# TODO: Import the custom 'fitness_tracker' module.
import fitness_tracker
# TODO: Ask the user to input the distance they walked, ran, and cycled today.
walk = float(input("distance walked"))
run = float(input("distance ran"))
cycle = float(input("distance cycled"))
# TODO: Calculate and print the total calories burned for each activity.
walk_calos = fitness_tracker.walk_calories(walk)
print(walk_calos)
run_calos = fitness_tracker.run_calories(run)
print(run_calos)
cycled_calos = fitness_tracker.cycle_calories(cycle)
print(cycled_calos)

# TODO: Sum and print the total calories burned for the day.
total_calories_burned = cycled_calos + run_calos + walk_calos
print(tota_calories_burned)

#------------------------------------------------------------------------------------
# Task 10: Using a while loop to Simulate Loan Repayment (Real-life Scenario: Paying Off a Loan)

# TODO: Ask the user to input the total loan amount.
# TODO: Ask the user to input their monthly repayment amount.
# TODO: Use a while loop to simulate monthly payments, reducing the loan each month.
# TODO: Print the remaining loan amount after each payment.
# TODO: When the loan is fully paid off, print a congratulatory message.

loan_amount = float(input("Enter the total loan amount: "))
monthly_payment = float(input("Enter your monthly payment amount: "))

# TODO: Use a while loop to simulate the repayment process.
if monthly_payment <= 0:
    print("Monthly payment must be more than than zero.")
else:
    while loan_amount > 0:
    loan_amount -= monthly_payment
if loan_amount < 0:
            loan_amount = 0
    
 print(f"Remaining loan amount: ${loan_amount:.2f}")


