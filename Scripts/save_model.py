import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load cleaned data
df = pd.read_csv('data/cleaned_resumes.csv')

# TF-IDF Vectorization
tfidf = TfidfVectorizer(max_features=3000)
X = tfidf.fit_transform(df['Cleaned_Resume'])
y = df['Category']

# Train the model
model = LogisticRegression()
model.fit(X, y)

# Save model and vectorizer
joblib.dump(model, 'models/resume_model.pkl')
joblib.dump(tfidf, 'models/tfidf_vectorizer.pkl')

print("✅ Model and vectorizer saved to 'models/' folder")
