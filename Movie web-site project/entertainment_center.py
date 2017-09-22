import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_longest_ride = media.Movie("The Longest Ride",
                               "It's a very romantic love story, between two different characters",
                               "https://en.wikipedia.org/wiki/The_Longest_Ride_(film)#/media/File:The_Longest_Ride_poster.png",
                               "https://www.youtube.com/watch?v=UggIMiXTe1Q&oref=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DUggIMiXTe1Q&has_verified=1")

movies = [toy_story, avatar, the_longest_ride]
fresh_tomatoes.open_movies_page(movies)
