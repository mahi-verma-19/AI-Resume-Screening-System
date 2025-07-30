import pandas as pd
import sys
sys.path.append('./Scripts')  # Add this line

from preprocess import preprocess


# Load the dataset
df = pd.read_csv("data/UpdatedResumeDataSet.csv")

print("🔍 First 3 rows of raw data:\n")
print(df.head(3))

# Show basic info
print("\n📊 Dataset Info:")
print("Total Resumes:", len(df))
print("Sample Categories:", df['Category'].unique())

# Drop missing
df.dropna(subset=['Resume', 'Category'], inplace=True)

print("\n✅ Nulls dropped. Remaining rows:", len(df))

# Apply preprocessing
print("\n🧠 Preprocessing resumes...")
df['Cleaned_Resume'] = df['Resume'].apply(preprocess)

# Show example
print("\n📄 Sample Cleaned Resume:\n")
print(df['Cleaned_Resume'].iloc[0])

# Save cleaned data
df.to_csv("data/cleaned_resumes.csv", index=False)
print("\n💾 Saved cleaned data to 'data/cleaned_resumes.csv'", flush=True)

# Keep the terminal open long enough to see output
input("\n🔚 Press Enter to exit...")
