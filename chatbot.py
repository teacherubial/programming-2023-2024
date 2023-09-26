# Chatbot
# Author: Ubial
# Date: 21 September 2023

# Greet the user
print("Hello there! 🤖")
print("I'm a crude chatbot, here to talk to you.")

# Get the user's name and store in a variable
user_name = input("So... what's your name? ")

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

print(list_of_fave_food_responses[22])

# Choose one reponse randomly from the list
import random
random_response = random.choice(list_of_fave_food_responses)

# Print out the chosen response
print(random_response)