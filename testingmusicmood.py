import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load your songs CSV file
songs = pd.read_csv('my_songs.csv')  # Make sure the file path is correct

# Ask user for their current mood
user_mood = input("🎧 What mood are you in? (e.g., happy, calm, sad): ")

# Vectorize moods
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(songs['mood'])
user_vec = vectorizer.transform([user_mood])

# Compute similarity
similarities = cosine_similarity(user_vec, tfidf_matrix).flatten()

# Get top 3 recommendations
top_indices = similarities.argsort()[::-1][:3]

print("\n🎵 Recommended Songs for Your Mood:\n")
for i in top_indices:
    print(f"{songs.iloc[i]['title']} by {songs.iloc[i]['artist']} (Match: {similarities[i]:.2f})")
