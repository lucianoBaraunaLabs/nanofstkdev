# -*- coding: utf-8 -*-

import media
import fresh_tomatoes

# Instancia de variábel toy_story
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# print(toy_story.storyline)
avatar = media.Movie("Avatar",
        "A marine on an alien planet",
        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

avenger_infintywar = media.Movie("Avengers: Infinity War",
                    "Having acquired the Power Stone, one of the six Infinity Stones",
                    "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                    "https://www.youtube.com/watch?v=t_ULBP6V9bg")

school_of_rock = media.Movie("School of Rock",
                "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Avengers: Infinity War",
              "Storyline",
              "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
              "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Avengers: Infinity War",
                    "Storyline",
                    "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                    "https://www.youtube.com/watch?v=FAfR8omt-CY")

movies = [toy_story, avatar, avenger_infintywar, school_of_rock, ratatouille, midnight_in_paris]

print (media.Movie.valid_ratings)
print (media.Movie.__doc__)

# fresh_tomatoes.open_movies_page(movies)