import streamlit as st
st.write("Hello☺️! This is a helpful daily schedule to help you be more: Fabulously Encouraging, Lovely, Incredible, Careing, Incomprehendibly Trustworthy, Yummilicious!")

st.checkbox("Wake up")

st.checkbox("brush teeth")
st.checkbox("brush hair")
checkbox = st.checkbox("Enable custom input")
if checkbox:
    user_input = st.text_input("Enter your custom text")
    if user_input:
        st.write(f"You entered: {user_input}")
