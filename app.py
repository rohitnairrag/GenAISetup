import google.generativeai as genai
import os
# get api from enviornment
key=os.getenv('GOOGLE_API_KEY')

#Configure the model
genai.configure(api_key=key)
model=genai.GenerativeModel('gemini-2.5-flash-lite')

# Create a frontend UI
import streamlit as st
st.title('SIMPLE TEXT GENERATION')
st.header('This is to test the gemini model as application')
promt=st.text_input('Write your input promt here',max_chars=10000)
response=model.generate_content(promt)
st.write(response.text)