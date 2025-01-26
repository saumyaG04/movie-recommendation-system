from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pandas as pd

def recommend_content_based(movie, data_path="C:\\Users\\saumy\\OneDrive\\Documents\\Python Projects\\portfolio\\movie recommendation system\\notebooks\\data\\cleaned_data.csv"):
    data = pd.read_csv(data_path)

    # Create a TF-IDF matrix for genres
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(data["genres"])

    # Train the NearestNeighbors model
    nn_model = NearestNeighbors(metric="cosine", algorithm="brute")
    nn_model.fit(tfidf_matrix)

    # Map movie titles to indices
    indices = pd.Series(data.index, index=data["title"]).drop_duplicates()

    # Check if the movie title exists
    if movie not in indices:
        return [f"Movie '{movie}' not found in the dataset."]

    # Get the index of the movie
    idx = indices[movie]

    # Find nearest neighbors
    distances, neighbors_indices = nn_model.kneighbors(tfidf_matrix[idx], n_neighbors=10)

    # Exclude the input movie itself
    similar_movies_indices = neighbors_indices.flatten()[1:]

    # Return recommended movie titles
    return data["title"].iloc[similar_movies_indices].tolist()
