import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()  # loading all environment variables


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load gimini model and get responses
model = genai.GenerativeModel("gemini-pro")


def gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Initialize streamlit app


st.set_page_config(page_title="Q&A Demo")
st.header("Gemini BOT")
input = st.text_input("Input: ", key="input")

submit = st.button("Submit")

# When submit button is clicked, get response from gemini model

if submit:
    response = gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
