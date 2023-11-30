import streamlit as st
import requests

#code to set the page
st.set_page_config(
    page_title="Cat App",
    page_icon=":cat:"
)

st.header("Welcome to my :cat: APP")

def get_content():
    """Access the API and get the image URL"""
    contents = requests.get('https://cataas.com//cat')
    #contents = requests.get('https://cataas.com//cat/gif')
    return contents.content

def place_image():
    cat_image = get_content()
    st.image(cat_image, width=200)

st.button("Click here",
          help="Click here to get a cat image",
          on_click=place_image)

