# Seth McCoy
# 4/7/2024
# P1HW2
# I will create a program that does some basic math on numbers that are entered.

# Ask user to enter their budget
budget = float(input("Enter budget: "))

# Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Ask user for amount they will spend on gas
gas_cost = float(input("How much do you think you will spend on gas? "))

# Ask user for amount they will spend on accommodation
accommodation_cost = float(input("Approximately, how much will you need for accomodation/hotel? "))

# Ask user for amount they will spend on food
food_cost = float(input("Lastly, how much do you need for food? "))

# Calculate total expenses
total_expenses = gas_cost + accommodation_cost + food_cost

# Display expenses for each category and remaining budget
print("")
print('-----------------------Travel Expenses-----------------------')
print("Location:", destination)
print("Initial Budget:", budget)
print("")
print("Fuel:", gas_cost)
print("Accommodation:", accommodation_cost)
print("Food:", food_cost)
print("")
print("Remaining Budget:", budget - total_expenses)