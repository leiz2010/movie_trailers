import media
import fresh_tomatoes


# Create six movie objects
seven_seal = media.Movie("The Seventh Seal",
                    "A man seeks answers about life, death, and the existence of God as he plays chess against the Grim Reaper during the Black Plague.",
                    "http://www.spicmacay.com/sites/default/files/cinema_posters/The-Seventh-Seal.jpg",
                    "https://www.youtube.com/watch?v=sWrPwI1EW7s",
                    "Ingmar Bergman",
                    "1958")

diary_of_a_country_priest = media.Movie("Diary of a Country Priest",
                        "An unwelcomed young priest and his encounters with the people of the community.",
                        "http://ia.media-imdb.com/images/M/MV5BNDU2MTE1NjAyNl5BMl5BanBnXkFtZTcwNzE4NjQyMQ@@._V1_SY317_CR5,0,214,317_AL_.jpg",
                        "https://www.youtube.com/watch?v=BGahlJKuAX8",
                        "Robert Bresson",
                        "1951")
                        

floating_weeds = media.Movie("Floating Weeds",
                            "A story of the boss of a travelling theater, his mistress, and their son.",
                            "http://upload.wikimedia.org/wikipedia/en/2/29/Floating_Weeds.jpg",
                            "https://www.youtube.com/watch?v=bHpVeD9kJEI",
                            "Yasujiro Ozu",
                            "1959")
                            
l_avventura = media.Movie("L'Avventura",
                         "A woman disappears during a Mediterranean boating trip, but her lover become attracted to her best friend during search.",
                         "http://image.tmdb.org/t/p/original/ydwsPMpeOwJoOAmW4fajcHuGkr9.jpg",
                         "https://www.youtube.com/watch?v=N6ShLDfjnzw",
                         "Michelangelo Antonioni",
                         "1960")

                         
mood_for_love = media.Movie("In the Mood for Love",
                       "Two neighbors, a woman and a man, form a strong bond after both suspect extramarital activities of their spouses. However, they agree to keep their bond platonic so as not to commit similar wrongs.",
                       "http://ia.media-imdb.com/images/M/MV5BMTk0MjY3NjEzN15BMl5BanBnXkFtZTYwNTk2NDI5._V1_.jpg",
                       "https://www.youtube.com/watch?v=o9wgUonzMac",
                       "Kar Wei Wong",
                       "2000")

ran = media.Movie("Ran",
                "An elderly lord abdicates to his three sons, and the two corrupt ones turn against him.",
                "http://upload.wikimedia.org/wikipedia/en/thumb/f/f2/Kuroran.jpg/220px-Kuroran.jpg",
                "https://www.youtube.com/watch?v=9q8kLDgoO_c",
                "Akira Kurosawa",
                "1985")                                                  

# Create a list of movies                                                                                                                                                                                                        
movies = [seven_seal, diary_of_a_country_priest, floating_weeds, l_avventura, mood_for_love, ran]

# Display movies in the list above
fresh_tomatoes.open_movies_page(movies)