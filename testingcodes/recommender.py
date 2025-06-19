import pandas as pd
from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split

# Sample ratings data: user, item, rating
ratings = [
    ('user1', 'movie1', 5),
    ('user1', 'movie2', 3),
    ('user2', 'movie1', 4),
    ('user2', 'movie3', 5),
    ('user3', 'movie2', 2),
    ('user3', 'movie3', 4),
]

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(pd.DataFrame(ratings, columns=['user', 'item', 'rating']), reader)

trainset, testset = train_test_split(data, test_size=0.25, random_state=42)

algo = KNNBasic(sim_options={'user_based': True})
algo.fit(trainset)

pred = algo.predict('user1', 'movie3')
print(f"Predicted rating for user1 on movie3: {pred.est:.2f}")
