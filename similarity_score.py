# Calculating Similarity Score
# Author: Ubial
# 9 November 2023

# Calculate similarity scores between two people

# Create two lists that represent the movies
# that they like
ubials_fave_movies = [
    "the matrix",
    "avengers: infinity war",
    "infernal affairs",
    "rogue one",
    "the empires strikes back"
]
bens_fave_movies = [
    "thomas and friends, big world big advanture",
    "paddington 2",
    "avengers: infinity war",
    "minions",
    "rogue one"
]

similarity_score = 0

# Increase similarity score if movies are the same
for movie in ubials_fave_movies:
    if movie in bens_fave_movies:
        similarity_score += 1

# Display the results
print(f"The similarity score between the users is:")
print(similarity_score)