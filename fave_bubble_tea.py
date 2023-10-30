# Bubble Tea Popularity Algorithm
# Author: Ubial
# Date: 27 October 2023

# Ask 5 users what their favourite bubble tea place is
# Print out a summary of the data

NUM_RESPONDENTS = 5

coco_likes = 0
chatime_likes = 0
suntea_likes = 0
xingfutang_likes = 0
bbqueen_likes = 0
other_likes = 0

for _ in range(NUM_RESPONDENTS):
    # Ask the user what their favourite bbt place is
    print("What's your favourite bubble tea place?")
    fave_bbt = input().strip(",.?! ").lower()

    # Tallying/Counting Algo
    # Options: CoCo, Chatime, SunTea, Xing Fu Tang, Bubble Queen
    # If they say CoCo, increase the counter for CoCo by one, etc.
    if fave_bbt == "coco":
        coco_likes = coco_likes + 1
    elif fave_bbt == "chatime":
        chatime_likes += 1
    elif fave_bbt == "suntea":
        suntea_likes += 1
    elif fave_bbt == "xing fu tang":
        xingfutang_likes += 1
    elif fave_bbt == "bubble queen":
        bbqueen_likes += 1
    else:
        other_likes += 1


coco_percentage = coco_likes / NUM_RESPONDENTS * 100
chatime_percentage = chatime_likes / NUM_RESPONDENTS * 100
suntea_percentage = suntea_likes / NUM_RESPONDENTS * 100
xingfutang_percentage = xingfutang_likes / NUM_RESPONDENTS * 100
bbqueen_percentage = bbqueen_likes / NUM_RESPONDENTS * 100
other_percentage = other_likes / NUM_RESPONDENTS * 100

# Print a summary of the results
print(f"CoCo Likes: {coco_likes} | {coco_percentage:.2f}%")
print(f"Chatime Likes: {chatime_likes} | {chatime_percentage:.2f}%")
print(f"Suntea Likes: {suntea_likes} | {suntea_percentage:.2f}%")
print(f"Xing Fu Tang Likes: {xingfutang_likes} | {xingfutang_percentage:.2f}%")
print(f"Bubble Queen Likes: {bbqueen_likes} | {bbqueen_percentage:.2f}%")
print(f"Other Likes: {other_likes} | {other_percentage:.2f}%")
