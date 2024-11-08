# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ["apple","kiwi","pear","banana"]
print(fruits)
# TODO: Add a fruit to the end of the list
fruits.append("pineaple")
# TODO: Insert a fruit at the beginning of the list
fruits.insert(0,"peach")
# TODO: Remove a fruit from the list
fruits.remove("kiwi")
# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
number = [1,2,3,4,5]
# TODO: Create a new list with each number squared
number = [1,2,3,4,5]
print(number)

for x in number :
    print(x**2)
       
# TODO: Find the sum and average of the original numbers
total = sum(number)
# TODO: Print the results
print(total)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
capdict = {"usa": "new york",
           "korea": "seoul",
           "south africa": "pretoria"
           }
print(capdict)
# TODO: Add a new country-capital pair
capdict["germany"] = "berlin"
print(capdict)
# TODO: Update the capital of an existing country
capdict.update({"usa": "new jersey"})
print(capdict)
# TODO: Remove a country-capital pair
capdict.popitem()
# TODO: Print the modified dictionary
print(capdict)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruitcolours_dict = {"kiwi" :"green",
                     "banana" :"yellow",
                     "peach" :"orange"
                     }
print(fruitcolours_dict)
# TODO: Print all the fruits (keys)
keys = fruitcolours_dict.keys()
print(keys)
# TODO: Print all the colors (values)
values = fruitcolours_dict.values()
print(values)
# TODO: Print each fruit and its color
items = fruitcolours_dict.items()
print(items)
# 
# TODO: Check if a fruit is in the dictionary and print its color
check = fruitcolours_dict.get("peach")
print(check)