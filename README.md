# AI Job Counselor

This project consists of two parts: a FastAPI backend and a Streamlit frontend.

## Setup

### FastAPI Backend

1. Navigate to the FastAPI directory: cd fastapi
2. Create a virtual environment: python -m venv venv
3. Activate the virtual environment:
- On Windows: `venv\Scripts\activate`
- On Unix or MacOS: `source venv/bin/activate`
4. Install the requirements: pip install -r requirements.txt
5. Run the FastAPI server: uvicorn main:app --reload

### Streamlit Frontend

1. Navigate to the Streamlit directory: cd streamlit
2. Create a virtual environment: python -m venv venv
3. Activate the virtual environment:
- On Windows: `venv\Scripts\activate`
- On Unix or MacOS: `source venv/bin/activate`
4. Install the requirements: pip install -r requirements.txt
5. Run the Streamlit app: streamlit run app.py

Visit `http://localhost:8501` in your browser to use the AI Job Counselor.