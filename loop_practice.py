# Loop Practice
# Author: Ubial
# Date: 10 October 2023

import time

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

countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "Happy New Year! 🎆"]

for line in countdown:
    print(line)
    # time.sleep(1)

names = ['Anthony Maldonado', 'Randy Love', 'Christopher Valdez', 'Rodney Odom', 'Kimberly Ramos', 'Lisa Ray', 'Kevin Terry', 'Gregory Romero', 'Debbie Harris', 'Edwin Hall', 'Mark Myers', 'Lisa Long', 'Stephanie Watson', 'Katherine Fields', 'Kathryn Olson', 'Maurice Baxter', 'Russell Caldwell', 'Heather Griffin', 'Kara Lane', 'Mark Tucker', 'Kathryn Rodriguez', 'Rachael Daniels', 'Debra Whitaker', 'Angela Neal', 'Michelle Hall', 'Jessica Olson', 'Lynn Jensen', 'Marc Ray', 'Valerie Harris', 'Tina Webb', 'Donna Green', 'Derek Mcgee', 'Tammy Hall DVM', 'Christopher Johnston', 'Eric Smith', 'Matthew Lopez', 'Mary Smith', 'Dr. Heather Ramos MD', 'Eric Johnson', 'Dylan Alvarado', 'Aaron Huff', 'Robin James', 'Sandra Stevens', 'Scott Thomas', 'Philip Nelson', 'Marcus Martin', 'Mary Alexander', 'Jason James', 'Samantha Burch', 'Jessica Martinez', 'Jose Wright', 'Zachary Pineda', 'William Ramos', 'Shelby Hughes', 'Melanie Moore', 'Kimberly Fowler', 'Jordan Jones', 'Brenda Anderson', 'Russell Coleman', 'Jeremy Snow', 'Billy Wu', 'Jesse Rodriguez', 'Andrew Shea', 'Jason Castillo', 'Donald Abbott', 'Richard Cervantes Jr.', 'Jeffrey Powell', 'Angel Fernandez', 'Michelle Donovan', 'Mr. Michael Wagner DDS', 'Kimberly Gonzalez', 'Thomas Smith', 'Nichole Barnes', 'Shelly Clark', 'Ashley Ortiz', 'Jessica Lam', 'Kimberly Ray MD', 'Mason Kennedy', 'Whitney Harrington', 'Nicole Tran', 'Robert Montgomery', 'Ryan Gardner', 'Kimberly Silva', 'Stephanie Rivera', 'William Santos', 'Ashley Mcclain', 'Sophia Williams', 'Kevin Herring', 'Tyrone Leonard', 'Carolyn Jones', 'Stephanie Willis', 'Jon Lang', 'Tammy Porter', 'Robert Garcia', 'Casey Brown', 'Benjamin Aguilar', 'Nancy Norman', 'Aaron Peters', 'Blake Graham', 'Noah Harper DDS', 'Dwayne Ortiz', 'Melissa Padilla', 'Rebecca Jones', 'Michael Wood', 'Daniel Bean', 'Alexander Kaufman', 'Michael Higgins', 'Richard Bailey', 'Jay Cisneros', 'Lisa Acevedo', 'Sarah Hernandez', 'Bryan Jones', 'Mark Kennedy', 'Robert Caldwell', 'Larry Wolf', 'Robert Adkins', 'Wanda Doyle', 'Thomas Brown', 'Kevin Key', 'Stacey Fisher', 'Amber Hart', 'Paul Russell', 'Jacqueline David', 'Shannon Parker', 'Lisa Sanchez', 'Jennifer Atkins', 'Jason Woods', 'Richard Garcia', 'Luis Williams', 'Marco Weaver', 'Amy Hayes', 'Elizabeth Doyle DDS', 'Nicole Smith', 'Karen Thomas', 'Randy Reese', 'Deanna Rodriguez', 'Christian Conway', 'Craig Doyle', 'Dennis Oneill', 'Diane Jordan', 'Patrick Holder', 'Christina Thompson', 'Deanna Lee', 'Kathleen Davis', 'Brian Cox', 'Kristen Thomas', 'Samantha Smith', 'William Moss', 'Matthew Flowers', 'Megan Powell', 'Richard Williamson', 'Cindy Glenn', 'John Taylor', 'Nathaniel Lee', 'Sara Glover', 'James Jackson II', 'Carlos Henderson', 'Edward Holder', 'Whitney Hansen', 'Matthew Jacobs', 'Raymond Rodriguez', 'Christy Kennedy', 'Lisa Johnson', 'Mark Harris', 'Stephen Bowers', 'Derrick Brown', 'Stephen Schroeder', 'Martin Lawrence', 'Brian Reed', 'Trevor Booker', 'Ruben Johnson', 'Jeffrey Griffith', 'William Townsend', 'Cynthia Park', 'Carla Yang', 'Oscar Hartman', 'Shawn Hendricks', 'Timothy Oconnor', 'Gina Robertson', 'Jennifer Rodriguez', 'Jared Harris', 'Austin Austin', 'Nathan Golden', 'Samantha Flores', 'Alexis Jones', 'Susan Rice', 'Randall Holmes', 'Connie Johnson', 'Carol Young', 'Brandon Norris', 'Timothy Lester', 'Dustin Mccarthy', 'Tammy Brock', 'Heather Cummings', 'John Moreno', 'Dawn Berry', 'Jeffrey Montes', 'Joshua Smith', 'Alexa Barber', 'Mark Lewis']

# Find "Deanna Lee"
person_to_find = "Deanna Lee"

for name in names:
    if name == person_to_find:
        print(f"We found {person_to_find}!")
        break
else:    # if we don't find the person
    print("We didn't find them...")

for _ in range(100):
    print("Mr. Ubial is cool.")

for i in range(10_000):
    print(i)

# Can we start at another number?
for i in range(-100, 0):
    print(i)

# Can we count by any other number?
for i in range(0, 101, 7):
    print(i)

# 1. Print all even numbers between 
#    1200 and 1500 inclusive.
#    Use a for loop.

# 2. Print all odd numbers between
#    -150 and 0 inclusive.

# Once you have your solution,
# copy and paste your answer in #i-made-this