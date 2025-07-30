import pandas as pd

# Load cleaned data
df = pd.read_csv('data/cleaned_resumes.csv')

# Show some rows to verify
print(df.head())
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Vectorize the cleaned resumes using TF-IDF
tfidf = TfidfVectorizer(stop_words='english', max_features=3000)
X = tfidf.fit_transform(df['Cleaned_Resume'])  # Features
y = df['Category']                             # Labels

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train a logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("\n📊 Classification Report:\n")
print(classification_report(y_test, y_pred))
print("🎯 Accuracy:", accuracy_score(y_test, y_pred))
