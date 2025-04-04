from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

## Load Gemini pro vision model
model=genai.GenerativeModel('gemini-1.5-pro')

def get_gemini_responce(input,image,user_prompt):
    response=model.generate_content([input,image[0],user_prompt])
    return response.text


def input_image_details(uploaded_file):
    if uploaded_file is not None:
        #Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        
        image_parts = [
            {
                "mime_type": uploaded_file.type, 
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

##initialize Streamlit app

st.set_page_config(page_title="Multil-Language Invoice Extractor")

st.header("Multil-Language Invoice Extractor")
input = st.text_input("Search From Invoice:", key="input")
uploaded_file = st.file_uploader("Choose an Image of Invoice", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    submit=st.button("Get Results")
    
    input_prompt=""" 
    you are an expert in understanding invoices. we will upload a image as invoice and you will have to answer
    any questions based on the uploaded invioces image.
    """
    
    ##If submit bvutton is clicked
    if submit: 
        image_data = input_image_details(uploaded_file)
        responce=get_gemini_responce(input_prompt,image_data,input)
        st.write(responce)