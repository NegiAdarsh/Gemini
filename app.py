from dotenv  import load_dotenv
load_dotenv()   ##loading all the env variables

import streamlit as st
import os 
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



##function to load gemini model and gemini model 2 
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_res(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q&A DEMO")

st.header("GEMINI SAMPLE APPLICATION")

input = st.text_input("Input: ",key="input")

submit  = st.button("Ask a question")

# when submit is clicked 
if submit:
    response = get_gemini_res(input)
    st.subheader("Response is ")
    st.write(response)
    


