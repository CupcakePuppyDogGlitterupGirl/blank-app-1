import streamlit as st

st.title("😎 Welcome to Uncle Zergei's Homeschool Programing Club for Girls!")

"""
We are so excited to have you joining us this year! Before you can be officially enrolled, 
we need to collect some information from you:
* Your full name
* Your age
* Your date of birth
* A photo for your official ID
* Which sports you have played so far
* Your favorite color
* Have you been on your official club visit yet?
"""

# EXAMPLE INPUT
full_name = st.text_input("What is your full name?")

age = st.slider("What is your age?")

birthday = st.date_input("When is your birthday?")

picture = st.camera_input("Take a picture")




# EXAMPLE OUTPUT
st.subheader("Student info")
st.write("Full name:", full_name)
st.write("Age:", age)
st.write("Birthday:", birthday)
if picture:
    st.image(picture, width=100)

