# AI-Resume-Screening-System
This project is a smart, AI-driven web application designed to automatically classify resumes into suitable job categories using Natural Language Processing (NLP) and Machine Learning. The goal is to assist HR departments, recruiters, or job portals in quickly identifying candidate fitment based on resume content.
The AI-Based Resume Screening System is a machine learning-powered web application that helps automate the initial phase of recruitment by classifying resumes into predefined job categories such as Data Science, Web Development, DevOps, Testing, etc.

This system enables HR professionals and recruiters to save time and effort by instantly analyzing resumes and categorizing them based on skillsets mentioned in the text.
 Objectives:
To reduce the manual effort required in resume screening

To classify resumes based on relevant keywords and domain knowledge

To build an easy-to-use interface for uploading and analyzing resumes

To apply natural language processing (NLP) for textual data preprocessing

Tools and Technologies Used:
✅ Frontend:
Streamlit: A Python-based open-source framework used to develop the web application UI with minimal code. It enables easy form handling, file uploads, and result display on the same page.

✅ Backend:
Python: The core programming language used for writing the logic, data handling, and model integration.

Libraries Used:

pandas: For data manipulation and loading CSV files.

numpy: For numerical operations.

scikit-learn: For machine learning algorithms such as TF-IDF vectorization and classification.

spaCy & nltk: For NLP preprocessing like tokenization, stopword removal, etc.

joblib: For saving and loading the trained ML model.

re: Regular expressions for data cleaning and formatting.

PyPDF2: For extracting text from PDF resumes.

✅ Machine Learning Model:
TF-IDF Vectorizer: To convert resume text into numerical features.

Support Vector Machine (SVM): For classification of resumes into job categories.

Model Training: Based on a labeled dataset of resumes with predefined categories.

✅ Dataset:
Downloaded from Kaggle: The dataset contains multiple resumes categorized into fields like Data Science, Web Development, DevOps, etc.

✅ Deployment:
Currently running locally using Streamlit

Can be deployed using:

Streamlit Cloud

Render

Heroku

GitHub Pages + Binder (for static demos)

🖼️ Output Interface:
The user-facing Streamlit app has:

A text box where the resume content is pasted or uploaded

A button: "Predict Category"

Output: The predicted job category based on the resume content

How to Use the System:
Launch the application using streamlit run scripts/App.py

Paste the resume text or upload a .pdf file

Click on Predict Category

View the predicted job field

💡 Advantages:
Speeds up the recruitment process

Standardizes resume screening

Removes human bias from initial filtering

Can be easily adapted to any company-specific job roles

📤 How Others Can Use This App:
You can deploy it online using Streamlit Cloud or Heroku and share the public URL.

Anyone with the link can upload/paste their resume and get categorized instantly.

