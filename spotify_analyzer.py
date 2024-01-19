# Spotify Data Analyzer
# Author: Ubial
# 16 January 2024

# Version 0.1
#   - From the data set, get all the songs
#     performed my Drake

import csv


def find_all_songs(artist: str) -> list:
    """Returns a list of all songs from a given artist."""

    # Open up the file
    with open("./spotify.csv") as f:
        # ---- Look for all songs from given artist
        #      Use linear search
        # Create a csv reader object
        csv_reader = csv.DictReader(f)

        # Create a list to store all Drake's songs
        songs = []

        # for every song in the .csv file
        for line in csv_reader:
            if artist.lower() in line["artist"].lower():
                # add it to the song list
                songs.append((line["artist"], line["song_title"], line["danceability"]))

        return songs


drake_songs = find_all_songs("Drake")
ed_sheeran_songs = find_all_songs("Ed Sheeran")
kendrick_songs = find_all_songs("Kendrick")

for song in kendrick_songs:
    if float(song[-1]) >= 0.6:
        print(song)

# Print out all songs that have
# a danceability of >= 0.6
