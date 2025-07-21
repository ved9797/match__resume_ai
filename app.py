import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() # activate the api key
genai.configure(api_key = os.getenv("GOOGLE_GEMINI_API_KEY"))

# Movie Recommender System
st.title("Movie Recommender System!!")
user_input = st.text_input("Enter the movie name")
submit = st.button("click here....")

model = genai.GenerativeModel("gemini-1.5-flash-002")

if submit:
    response = model.generate_content(f"Generate Movie Recommendations for {user_input}")
    st.write(f"Recommendations:{response}")
else:
    st.write(" ")