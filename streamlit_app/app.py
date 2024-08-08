import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="AI Job Counselor", page_icon=":briefcase:", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
        padding: 20px;
    }
    .stButton>button {
        color: white;
        background-color: #4CAF50;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    .stTextArea>textarea {
        font-size: 16px;
        background-color: #f8f9fa;
        color: #000;
        border: 1px solid #ced4da;
        border-radius: 8px;
    }
    .stAlert {
        background-color: #f8f9fa;
        color: #000;
        border: 1px solid #ced4da;
        border-radius: 8px;
    }
    .st-bx {
        font-size: 1rem;
        font-weight: 600;
        color: #495057;
        text-align: left;
    }
    .tips {
        font-size: 1rem;
        font-weight: 400;
        color: #6c757d;
        padding: 10px;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #212529;
    }
    p, div, span {
        color: #212529;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description with an icon
st.title("🧑‍💼 AI Job Counselor")
st.markdown("### Get personalized job recommendations based on your input")

# Use columns to organize content
col1, col2 = st.columns([2, 1])

with col1:
    user_input = st.text_area("Describe your skills, interests, and experience:", height=200, help="Provide as much detail as possible for the best results.")

with col2:
    st.markdown("### Tips for better results:")
    st.markdown(
        """
        <ul class="tips">
            <li>Be as specific as possible.</li>
            <li>Mention your key skills and interests.</li>
            <li>Include any relevant experience.</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

def get_emoji(predicted_job):
    if predicted_job == "Athlete":
        return "🏃‍♂️"
    elif predicted_job == "Teacher":
        return "👩‍🏫"
    elif predicted_job == "Construction Worker":
        return "👷‍♂️"
    elif predicted_job == "Lawyer":
        return "👨‍💼"
    else:
        return "❓"

if st.button("Get Job Prediction"):
    with st.spinner('Analyzing your input...'):
        try:
            response = requests.post("http://127.0.0.1:8000/predict", json={"text": user_input})
            response.raise_for_status()  # Raise an error for bad HTTP status codes
            prediction = response.json()['prediction']
            emoji = get_emoji(prediction)
            
            st.success(f"Predicted Job: {emoji} **{prediction}**")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
            st.warning("Please make sure your FastAPI server is running and the endpoint is correct.")
