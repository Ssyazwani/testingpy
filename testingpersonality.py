import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# ----------------------------
# Step 1: Define Questions
# ----------------------------
questions = [
    "You prefer to spend time (a) with friends or (b) alone:",
    "You usually (a) plan everything or (b) go with the flow:",
    "You make decisions based on (a) logic or (b) feelings:",
    "In a group project, you prefer to (a) lead or (b) support:",
    "You are more (a) practical or (b) imaginative:"
]

# ----------------------------
# Step 2: Generate Fake Training Data
# ----------------------------
def generate_fake_data(n=200):
    data = []
    for _ in range(n):
        answers = [random.choice([0, 1]) for _ in range(5)]  # 0 = 'a', 1 = 'b'
        personality = "Introvert" if sum(answers) > 2 else "Extrovert"
        data.append(answers + [personality])
    columns = [f"Q{i+1}" for i in range(5)] + ["Personality"]
    return pd.DataFrame(data, columns=columns)

df = generate_fake_data()

# ----------------------------
# Step 3: Train the Classifier
# ----------------------------
X = df.drop("Personality", axis=1)
y = df["Personality"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# ----------------------------
# Step 4: Quiz and Prediction
# ----------------------------
print("🧠 Personality Quiz")
print("Answer with 'a' or 'b'\n")

user_answers = []

for q in questions:
    while True:
        ans = input(q + " ").strip().lower()
        if ans in ['a', 'b']:
            user_answers.append(0 if ans == 'a' else 1)
            break
        else:
            print("Please answer with 'a' or 'b' only.")

prediction = model.predict([user_answers])
print("\n✅ Your predicted personality type is:", prediction[0])
