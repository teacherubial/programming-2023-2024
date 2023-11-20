# Parental Bot

# Create list of questions
questions = [
    "Did you eat? ",
    "Did you study? ",
    "Did you do your laundry? ",
    "Did you call grandma? ",
]

score = 0

# Question algo
for question in questions:
    response = input(question).lower().strip()

    # Postive response
    if response == "yes":
        score += 1

if score >= 3:
    print("Good!")
elif score >= 1:
    print("OK.")
else:
    print("I'm coming over.")
