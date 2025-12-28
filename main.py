import streamlit as st
import openai as OpenAI
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import re
import pandas as pd  


load_dotenv()
client = OpenAI.Client(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="PDF Q&A", page_icon="📄", layout="wide")
st.title("📄 PDF resume analyzer")
st.markdown("Upload a PDF and ask questions about its content!")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")   

if uploaded_file :
    pdf = PdfReader(uploaded_file)
    text = ""
    for page in pdf.pages:
        page_text = page.extract_text() + "\n"
        if page_text:
            text += page_text


    text_clean = re.sub(r"(?<!\n)\n(?!\n)", " ", text)

    col1 , col2 = st.columns([1,1])

    with col1:
        st.subheader("Extracted Text")
        st.text_area("PDF Content", text_clean, height=400)

    with col2:
        st.subheader("AI analysis")
        if st.button("Analyze PDF"):
            with st.spinner("Analyzing..."):
                prompt = f"""
                You are a resume expert.
                Analyze the following resume provide:
                1. A summary of the candidate's qualifications.
                2. Key skills and experiences.
                3. Suggestions for improvement.
                4. A score out of 10 based on industry standards.
                   - Summary
                   - skills match 
                   - experience match
                   - clarity and presentation
                   - overall impression
                Provide the individual scores in a JSON:
                Resume:
                {text_clean}
                """
                
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=700
                )
                result = response.choices[0].message.content

                parts = result.split("Score JSON:")
                analysis_text = parts[0]
                st.write(analysis_text)

                if len(parts) > 1:
                    try:
                        import json
                        score_json = json.loads(parts[1].strip())
                        st.subheader("Score Breakdown")
                        df = pd.DataFrame({
                            "Category" : list(score_json.keys())
                            ,"Score" : list(score_json.values())
                        })
                        st.bar_chart(df.set_index("Category"))

                        st.subheader("Overall Score")
                        total_score = sum(score_json.values()) 
                        st.progress(min(total_score / 100), 1.0)

                    except:
                        st.warning("Could not parse score JSON.")