# Chatbot
# Author: Ubial
# Date: 21 September 2023

import random
import time

# Greet the user
# Pause in between lines of dialogue
print("Hello there! 🤖")
time.sleep(2)
print("I'm a crude chatbot, here to talk to you.")
time.sleep(1.5)

# Get the user's name and store in a variable
user_name = input("So... what's your name? ")
time.sleep(2)

# Respond with the user's name
print(f"It's nice to meet you, {user_name}!")

# Ask the user what their favourite food is
fave_food = input("What's your favourite food? ")

# Respond with something that is NOT TOO repetitive
# Create a list of appropriate responses
list_of_fave_food_responses = [
    "Mmmmmm. That sounds delicious.",
    f"Yes, {fave_food} is one of my favourites, too!",
    "Cool.",
    "Interesting, I've never tried that before."
]

# Choose one reponse randomly from the list
random_response = random.choice(list_of_fave_food_responses)

# Print out the chosen response
print(random_response)