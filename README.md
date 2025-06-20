# Movie Recommendation System

This is a simple movie recommendation system built with Python and Streamlit. It uses collaborative filtering to recommend movies to users based on their ratings and the ratings of similar users.

## Features

- Recommends movies to users based on their preferences
- User-based collaborative filtering using cosine similarity
- Simple Streamlit web interface
# Try the Movie Recommendation System Online!

You can try the app here:  
[Movie Recommendation System Streamlit App](https://movierecommendationsystem-4x5hdnnmpfxvnonukf35be.streamlit.app/)

# How It Works

This movie recommendation system uses **user-based collaborative filtering** with cosine similarity:

1. **Data Preparation**  
   The app loads a dataset of user ratings for movies. Each row contains a user ID, movie ID, movie name, and the user's rating for that movie.

2. **Building the Ratings Matrix**  
   The ratings are organized into a matrix where each row represents a user and each column represents a movie. The values are the ratings given by users to movies.

3. **Calculating User Similarity**  
   The system calculates how similar each pair of users is by comparing their ratings using **cosine similarity**. Users with similar tastes will have higher similarity scores.

4. **Finding Recommendations**  
   For a selected user, the system looks at the movies rated highly by the most similar users (but not yet rated by the selected user). It then recommends the top movie(s) based on these weighted ratings.

5. **User Interface**  
   Through the Streamlit app, you can select a user and get a movie recommendation instantly.

**In summary:**  
The app recommends movies to a user by finding other users with similar tastes and suggesting movies those similar users liked, but the current user hasn't seen yet.
