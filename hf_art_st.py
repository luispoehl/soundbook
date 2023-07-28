import os
import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import time
import uuid

API_URL = "https://api-inference.huggingface.co/models/prompthero/openjourney-v4"
token = st.secrets["token"]
headers = {"Authorization": token}

if 'generated_image' not in st.session_state:
    st.session_state['generated_image'] = None
if 'query' not in st.session_state:
    st.session_state['query'] = ''
if 'style' not in st.session_state:
    st.session_state['style'] = ''

def generate_uid():
    return str(uuid.uuid4())

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Function to query the Huggingface model and generate an image
def generate_image(user_input):
    image_bytes = query({
        "inputs": user_input,
    })
    image = Image.open(BytesIO(image_bytes))
    #image.show(title=user_input)
    return image


# Streamlit app
def main():
    print(os.getcwd())
    st.title("Huggingface Model Image Generation")
    query = st.text_input("Enter your query:",value=st.session_state['query'])
    style = st.text_input("Enter your style:",value=st.session_state['style'])

    st.session_state['query'] = query
    st.session_state['style'] = style

    query = f"{query} {style}"

    generate_button = st.button("Generate Image")

    if generate_button:
        generated_image = generate_image(query)
        st.session_state['generated_image'] = generated_image
        st.image(generated_image, caption="Generated Image", use_column_width=True)
        st.write(f"Query: {query}")

    if st.button("Save Image and Query"):
        title = generate_uid()
        st.write("i try to save now")
        st.session_state['generated_image'].save(f"./generated_images/{title}.png")
        with open(f"./generated_images/{title}.txt", "w") as file:
            file.write(query)
        st.success("Image and query have been saved successfully!")


if __name__ == "__main__":
    main()
