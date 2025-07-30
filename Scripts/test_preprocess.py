from preprocess import preprocess

sample_text = """
Experienced Python Developer with expertise in data analysis, machine learning, and backend development.
Proficient in Pandas, Scikit-learn, and REST APIs.
"""

processed = preprocess(sample_text)
print("Processed Text:\n", processed)
