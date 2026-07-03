import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")

cv = CountVectorizer()
matrix = cv.fit_transform(movies["genre"])

similarity = cosine_similarity(matrix)

def recommend(movie_name):
    if movie_name not in movies["title"].values:
        print("Movie not found!")
        return

    index = movies[movies["title"] == movie_name].index[0]

    distances = list(enumerate(similarity[index]))

    distances = sorted(distances, key=lambda x: x[1], reverse=True)

    print(f"\nRecommended Movies for '{movie_name}':\n")

    count = 0
    for movie in distances[1:]:
        print(movies.iloc[movie[0]].title)
        count += 1
        if count == 5:
            break

movie = input("Enter Movie Name: ")
recommend(movie)
