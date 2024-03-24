#!/usr/bin/env python

import sys

# Initialize variables to store current year, current movie, total rating, and count of ratings
current_year = None
current_movie = None
total_rating = 0
count = 0

# Read input from standard input
for line in sys.stdin:
    # Split the input line into individual fields
    year, movie_title, rating, rating_count = line.strip().split('\t')

    # Convert rating and rating count to float and integer, respectively
    rating = float(rating)
    rating_count = int(rating_count)

    # If the year or movie changes, print the result for the previous movie
    if current_year != year or current_movie != movie_title:
        if current_year and current_movie:
            # Calculate the average rating for the movie
            average_rating = total_rating / count
            # Print the result for the previous movie
            print(f"{current_year}\t{current_movie}\t{average_rating}")

        # Update variables for the new movie
        current_year = year
        current_movie = movie_title
        total_rating = 0
        count = 0

    # Accumulate the total rating and count of ratings for the current movie
    total_rating += rating
    count += rating_count

# Print the result for the last movie
if current_year and current_movie:
    average_rating = total_rating / count
    print(f"{current_year}\t{current_movie}\t{average_rating}")
