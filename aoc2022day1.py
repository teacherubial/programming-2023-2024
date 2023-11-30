# AOC Day 1
# Author: Ubial
# 30 November 2023

# There is one elf carrying the most calories
# How many does that one have?

# Create a list that holds all the calories of the
# elves

# Create a list to hold all calories of elves
elves = []

# Open the file
with open("./aoc2022day1.txt") as f:
    # Calories of the current elf
    current_cals = 0

    for line in f:
        # If there is something in the line
        if line.strip():
            current_cals += int(line.strip())
        else:
            # dump current_cals into elves list
            elves.append(current_cals)
            
            # reset current_cals for next elf
            current_cals = 0

print(elves)
print(max(elves))

# get the top three and sum them
sorted_elves = sorted(elves)
top_three = sorted_elves[-3:]
top_three_total = sum(top_three)

print(sum(sorted(elves)[-3:]))


