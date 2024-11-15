from streamlit_extras.let_it_rain import rain 

import streamlit as st

st.balloons()
st.snow()
def emojis():
    rain(
        emoji="❄️ ",
        font_size=54,
        falling_speed=5,
        animation_length="infinite"
    )
    
emojis()

st.title("It looks like everyone's white Christmas dreams will come true this year! Happy Holidays! This is San Taclause, from Ultra Sooper-Dooper Cool Mega News; signing off!")