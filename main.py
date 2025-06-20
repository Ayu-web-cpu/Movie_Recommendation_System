import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import random

df = pd.read_csv('movie_ratings_5000_with_names.csv')
df['movie_id'] = df['movie_id'].astype(str)
df['user_id'] = df['user_id'].astype(str)
ratings_matrix = df.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)
user_similarity = cosine_similarity(ratings_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=ratings_matrix.index, columns=ratings_matrix.index)
movie_id_to_name = df.drop_duplicates('movie_id').set_index('movie_id')['movie_name'].to_dict()

def recommend_movies(user_id, num_recommendations=1):
    user_id = str(user_id)
    if user_id not in ratings_matrix.index:
        print("User not found.")
        return []
    sim_scores = user_similarity_df[user_id].drop(user_id)
    similar_users = sim_scores.sort_values(ascending=False).index
    user_movies = set(ratings_matrix.loc[user_id][ratings_matrix.loc[user_id] > 0].index)
    recommendations = {}
    for sim_user in similar_users:
        sim_user_ratings = ratings_matrix.loc[sim_user]
        for movie_id, rating in sim_user_ratings.items():
            if movie_id not in user_movies and rating > 0:
                if movie_id not in recommendations:
                    recommendations[movie_id] = 0
                recommendations[movie_id] += rating * user_similarity_df.loc[user_id, sim_user]
        if len(recommendations) >= num_recommendations * 2:
            break
    recommended_movies = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    recommended_movie_ids = [movie_id for movie_id, _ in recommended_movies[:num_recommendations]]
    recommended_movie_names = [movie_id_to_name.get(movie_id, "Unknown") for movie_id in recommended_movie_ids]
    return list(zip(recommended_movie_ids, recommended_movie_names))

# Pick a random user with at least one unrated movie
valid_users = []
for test_user in ratings_matrix.index:
    user_movies = set(ratings_matrix.loc[test_user][ratings_matrix.loc[test_user] > 0].index)
    if len(user_movies) < len(ratings_matrix.columns):
        valid_users.append(test_user)
if not valid_users:
    print("No users with unrated movies found in the dataset.")
    exit()
random_user_id = random.choice(valid_users)

try:
    user_input = input(f"Enter user ID (or press Enter for random user {random_user_id}): ").strip()
except EOFError:
    user_input = ""

if user_input == "":
    user_id = random_user_id
else:
    user_id = user_input

if user_id not in ratings_matrix.index:
    print("User ID not found in the dataset.")
else:
    recommended = recommend_movies(user_id, num_recommendations=1)
    print(f"Recommended movie for user {user_id}:")
    if recommended:
        movie_id, movie_name = recommended[0]
        print(f"{movie_id}: {movie_name}")
    else:
        print("No recommendation available for this user.")