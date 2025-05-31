import csv
import random
import pandas as pd

# Mood keywords list
mood_keywords = [
    "happy", "upbeat", "energetic", "cheerful", "joyful", "bright", "lively", "fun", "playful", "optimistic",
    "calm", "peaceful", "relaxing", "mellow", "smooth", "soothing", "chill", "dreamy", "gentle", "ambient",
    "sad", "emotional", "melancholy", "heartbreak", "gloomy", "wistful", "blue", "lonely", "reflective", "somber",
    "romantic", "love", "passionate", "tender", "intimate", "affectionate", "soulful", "warm", "longing",
    "dark", "intense", "mysterious", "haunting", "brooding", "dramatic", "powerful", "edgy", "aggressive", "raw",
    "pump-up", "dance", "party", "hype", "fast", "driving", "bold", "fierce", "vibrant",
    "fantasy", "mystical", "retro", "vintage", "experimental", "quirky", "inspirational"
]

# Read songs from CSV
songs_df = pd.read_csv('songs.csv')

print("Do you want to assign moods manually or randomly? (m/r): ")
choice = input().lower()

moods_list = []

for idx, row in songs_df.iterrows():
    title = row['title']
    artist = row['artist']

    if choice == 'm':
        moods = input(f"Enter moods for '{title}' by {artist} (separate with spaces): ").strip()
    else:
        moods = ' '.join(random.sample(mood_keywords, random.randint(2, 4)))
        print(f"Assigned moods for '{title}': {moods}")

    moods_list.append(moods)

# Add moods column to dataframe
songs_df['mood'] = moods_list

# Save updated CSV
songs_df.to_csv('songs_with_moods.csv', index=False)
print("\nSaved songs with moods to 'songs_with_moods.csv'")
