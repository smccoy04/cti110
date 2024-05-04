# Seth McCoy
# 4/13/2024
# P4HW1
# I will be adding onto previous assignment P2HW2.

# Get the number of scores from the user.
n = int(input("How many scores do you want to enter? "))

# Declare a list to store to the numbers.
score = []

# Get the score from user.
# Check if they lie between 1 to 100.
# If yes then add it to the list.
# else get score until a correct number is entered.
# Repeat steps 3 to 6 until all the scores are entered.
for i in range(n):
    # Prompts the user to enter a score and stores it in a variable s
    # since i starts from 0 we have used (i+1)
    # so that first score will not be printed as enter a score #0.
    s = int(input("Enter a score #" + str(i + 1) + ": "))
    
    # Now checks if score lies between 1-100.
    # if not then enter the loop prints an error message and prompts user until a correct score is entered.
    while s < 1 or s > 100:
        print("\nINVALID Score entered!!!!\nScore should be between 0 and 100")
        s = int(input("Enter score #" + str(i + 1) + " again: "))
    
    # After getting a correct score we convert it to float and add it to the list.
    score.append(float(s))

# Print the minimum number in the list.
low = min(score)

# listName.remove(element) removes the first occurrence of the element that is passed from the list.
score.remove(low)

# Calculate average.
average = sum(score) / len(score)

# Determine letter grade for average
if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
elif average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display results
print("")
print('------------------Results------------------')
print(f"Lowest Score  :      {low:<34.2f} ")
print(f"Modified List :      {score} ")
print(f"Scores Average:      {average:<34.2f} ")
print(f"Grade         :      {letter_grade:<34} ")
print("-------------------------------------------")