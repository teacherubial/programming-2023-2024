# Ask the user what their favourite food is
fave_food = input("What's your favourite food? ")

# If they say pizza, say something related to pizza
if fave_food == "pizza":
    print("🍕")
elif fave_food == "burgers":
    print("🍔")
else:
    print("I like that food!")

user_response = input("Are you happy? ")

if user_response == "yes":
    user_happy = True
else:
    user_happy = False

if user_happy:
    print("I like your smile.")
else:
    print("I hope you have a better day.")