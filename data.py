import pandas as pd
import numpy as np

# Sample movie list
movies = [
    (1, "The Shawshank Redemption"),
    (2, "The Godfather"),
    (3, "The Dark Knight"),
    (4, "Pulp Fiction"),
    (5, "Forrest Gump"),
    (6, "Inception"),
    (7, "Fight Club"),
    (8, "The Matrix"),
    (9, "Goodfellas"),
    (10, "The Lord of the Rings: The Return of the King")
]

num_users = 100
num_ratings = 5000

np.random.seed(42)

data = []
for _ in range(num_ratings):
    user_id = np.random.randint(1, num_users + 1)
    movie_id, movie_name = movies[np.random.randint(0, len(movies))]
    rating = np.random.choice([1, 2, 3, 4, 5])
    data.append([user_id, movie_id, movie_name, rating])

df = pd.DataFrame(data, columns=['user_id', 'movie_id', 'movie_name', 'rating'])
df.to_csv('movie_ratings_5000_with_names.csv', index=False)
print("Sample dataset 'movie_ratings_5000_with_names.csv' created.")
