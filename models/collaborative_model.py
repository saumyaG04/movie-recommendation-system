from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

def recommend_collaborative(movie, data_path="C:\\Users\\saumy\\OneDrive\\Documents\\Python Projects\\portfolio\\movie recommendation system\\notebooks\\data\\cleaned_data.csv"):
    data = pd.read_csv(data_path)
    
    # Pivot the data to create a user-item matrix
    user_item_matrix = data.pivot(index="user_id", columns="title", values="rating").fillna(0)
    
    # Compute cosine similarity between items
    similarity_matrix = cosine_similarity(user_item_matrix.T)

    # Create a mapping of movie titles to indices
    indices = pd.Series(range(len(user_item_matrix.columns)), index=user_item_matrix.columns)

    # Check if the movie exists
    if movie not in indices:
        return [f"Movie '{movie}' not found in the dataset."]

    # Get the index of the movie
    idx = indices[movie]

    # Get similarity scores for all movies
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Exclude the input movie itself
    sim_scores = sim_scores[1:11]

    # Return the top 10 most similar movies
    movie_indices = [i[0] for i in sim_scores]
    return user_item_matrix.columns[movie_indices].tolist()
