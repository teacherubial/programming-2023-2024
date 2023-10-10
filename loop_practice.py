# Loop Practice
# Author: Ubial
# Date: 10 October 2023

# Create a list of groceries
groceries = ["hot wheels", "lego", "ice cream", "video games"]

# Do something for each thing in the list
# Print it out in a pretty way
#   e.g.   * hot wheels
#            ---
#          * lego
#            ---

for item in groceries:
    print(f"* {item}")
    print("  ---")

# Create a pyramid like this using a for loop.

# *
# **
# ***
# ****
# *****

stars = ["*", "**", "***", "****", "*****"]

for row in stars:
    print(row)

# Problem:
# Create a new years eve countdown that's automated
# Requirements:
#  * Starts off at 10
#  * Countdown every second and print the second that it's at
#  * Instead of reaching zero it says "Happy New Year"
# Example Output:
#    10
#    9
#    8
# ...
#    1
#    Happy New Year!

