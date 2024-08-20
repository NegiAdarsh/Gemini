from dotenv  import load_dotenv
load_dotenv()   ##loading all the env variables

import streamlit as st
import os 
import google.generativeai as genai

from PIL import Image


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



##function to load gemini model and gemini model 2 
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_res(input,image):
    if(input!=""):
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)

    return response.text

st.set_page_config(page_title="GEMINI GENERATION")

st.header("WELCOME TO BLOGS")

input = st.text_input("Input: ",key="input")

uploaded_image = st.file_uploader("Choose an image file", type=['png', 'jpg', 'jpeg'])
image=""

# Display the uploaded image
if uploaded_image is not None:
    # # Display image details
    # st.write("Filename:", uploaded_image.name)
    # st.write("File type:", uploaded_image.type)
    # st.write("File size:", uploaded_image.size, "bytes")
    
    # Display the image
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    
submit  = st.button("Generate")

# when submit is clicked 
if submit:
    response = get_gemini_res(input,image)
    st.subheader("Generated Blog is: ")
    st.write(response)
    


