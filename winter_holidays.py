# Winter Holidays Review
# Author: Ubial
# 8 January 2024

# Requirements:
#  - create a function called winter_holiday()
#  - take one parameter
#      - string
#  - return a summary of an event from your holidays

# generated by chatgpt

import random


def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24

    Params:
        good_or_bad - indicate what kind of event to summarize

    Returns:
        an event that happened during the holidays
        the event is selected randomly"""


def main() -> None:
    print(winter_holiday("good"))
    # "I got a lego set for Christmas."
    # "I went to Richmond Centre to walk around aimlessly."

    print(winter_holiday("bad"))
    # "I asked for a bidet for Christmas instead I got a rando amazon smart watch."
    # "I hoped to snowboard but got lots of rain on the mountains instead."


if __name__ == "__main__":
    main()
