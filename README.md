# AI-RESUME-ANALYZER-using-STREAMLIT
A PDF resume analyzer using Python that extracts and cleans resume data with PyPDF2, regex, and pandas, and leverages OpenAI models for semantic analysis and job matching. Built a Streamlit-based UI for uploading resumes and displaying structured insights, enabling faster and more accurate candidate evaluation.


How to run

# AI Resume Analyzer

An AI-powered PDF resume analyzer built using Python, Streamlit, and OpenAI.  
The application extracts resume content, performs NLP-based analysis, and evaluates resumes against job descriptions.

## Features
- PDF resume upload and parsing
- Text cleaning using regex
- Skill and keyword extraction
- Semantic job-role matching using OpenAI
- Interactive Streamlit UI

## Tech Stack
- Python
- Streamlit
- OpenAI API
- PyPDF2
- pandas

## How It Works
1. User uploads a PDF resume
2. Text is extracted and cleaned
3. Resume content is analyzed using NLP and OpenAI
4. Results are displayed in a structured UI

## Setup Instructions
```bash
pip install -r requirements.txt
streamlit run main.py
