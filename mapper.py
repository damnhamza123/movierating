#!/usr/bin/env python

import sys

# Initialize a dictionary to store ratings and counts for each movie and year
movie_ratings = {}

# Read input from standard input
for line in sys.stdin:
    # Split the input line into individual fields
    fields = line.strip().split()

    # Extract movie title, year, and rating from the input
    movie_title = fields[1]
    year = fields[3]
    rating = float(fields[4])

    # Check if the movie has already been rated in this year
    if (movie_title, year) in movie_ratings:
        # If so, update the sum of ratings and count of ratings for the movie and year
        movie_ratings[(movie_title, year)][0] += rating
        movie_ratings[(movie_title, year)][1] += 1
    else:
        # If not, add a new entry for the movie and year with the initial rating and count
        movie_ratings[(movie_title, year)] = [rating, 1]

# Emit key-value pairs for each movie and year with the aggregated rating and count
for (movie_title, year), (total_rating, count) in movie_ratings.items():
    print(f"{year}\t{movie_title}\t{total_rating}\t{count}")
