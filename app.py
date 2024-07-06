import streamlit as st 
import google.generativeai as genai
from openai import OpenAI
from apikey import google_gemini_api_key, openai_key
client = OpenAI(api_key= openai_key)
genai.configure(api_key=google_gemini_api_key)


#code 
generation_config = {
  "temperature": 0.6,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

st.set_page_config(layout="wide")

#title
st.title(' A4Ani Cricket Blog Companion')

#Sub talk
st.subheader("Your one stop solution for Crciket. Now you can generate your content if you ran out of on1!!!")

#sidebar for user input
with st.sidebar:
    st.title("You can prompt here! ")
    st.subheader("Please let your assisstant know what you wanna get. Remember to be concise, ask one at a time and respectful!")
    
    blog_title = st.text_input(" CricInfo Blog title")
    
    keywords = st.text_input("Keywords (comma-separated)")
    
    num_of_words = st.slider("Number of words", min_value=300, max_value=1500,step=250)
    
    num_of_images = st.slider("Number of images", min_value=1,max_value=20,step=1)
    
    history=[
        {
            "role": "user",
            "parts": [
                f"Generate a comprehensive, engaging blog post relevent to \"{blog_title}\" Make sure to incorporate these keywords \"{keywords}\" in the blog post. The blog content should have {num_of_words} words in length.Ensure the content is informative, and maintains a consistent tone throughout , and harmless to anyone",
            ],
        },
    ]

    
    submit = st.button("Click here for magic")
    
if submit:  
    response = model.generate_content(history)
    images=[]
    
    for i in range(num_of_images):
        img_response = client.images.generate(
        model="dall-e-3", 
        prompt=f"Generate a blog Image on {blog_title}",
        size="1024x1024",           
        quality="standard",
        n=1,
        )
        images.append(img_response.data[0].url)
    
    
    for j in range(num_of_images):
        st.write(images[i])

    #st.image(img_url, caption = "Your generated image")
    
    st.title("Your esteemed Cricket Blog")
    st.write(response.text) 
        
    