# AI Job Counselor

This project consists of two parts: a FastAPI backend and a Streamlit frontend.

## General Setup

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

## Model Setup

The model files are not included in this repository due to their large size. Please follow these steps to set up the model:

1. Download the model files from [this Google Drive link](<https://drive.google.com/drive/folders/1A1nN6gjdUlbSvfX1ssbv1MWDBmoP_He8?usp=sharing>).
2. Create a folder named `model` inside the `fastapi_app` directory if it doesn't exist.
3. Extract the downloaded files and place them inside the `fastapi_app/model` directory.

Your directory structure should look like this after adding the model files:
fastapi_app/
├── model/
│   ├── distilbert-finetuned-four-v4/
│   │   ├── config.json
│   │   ├── model.safetensors
│   │   ├── special_tokens_map.json
│   │   ├── tokenizer_config.json
│   │   └── vocab.txt
│   └── ...
├── ...