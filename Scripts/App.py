import streamlit as st
import sys
sys.path.append('./scripts')

from preprocess import preprocess
import joblib
# Load the model and vectorizer
model = joblib.load('models/resume_model.pkl')
vectorizer = joblib.load('models/tfidf_vectorizer.pkl')

st.title("📄 AI-Based Resume Classifier")

# File uploader
uploaded_file = st.file_uploader("Upload your Resume (TXT or PDF only)", type=['txt', 'pdf'])

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        import PyPDF2
        reader = PyPDF2.PdfReader(uploaded_file)
        resume_text = ""
        for page in reader.pages:
            resume_text += page.extract_text()
    else:
        resume_text = uploaded_file.read().decode("utf-8")


    st.text_area("📋 Extracted Resume Text", resume_text, height=250)

    if st.button("Predict Category"):
        if resume_text.strip() == "":
            st.warning("⚠️ Resume is empty!")
        else:
            clean_text = preprocess(resume_text)
            vect_text = vectorizer.transform([clean_text])
            prediction = model.predict(vect_text)[0]
            st.success(f"✅ Predicted Job Category: **{prediction}**")
