import streamlit as st
import random

def get_roll(roll):
    if roll == 8:
        roll = "6"
    elif roll >= 5:
        roll = "4"
    elif roll >= 3:
        roll = "3"
    elif roll >= 1:
        roll = "1"
    else:
        roll = "2"
    return roll

roll = st.slider("How many sides does this dice have?")

roll = get_roll(roll)

st.write(roll)

# HOMEWORK: Make the get_roll function work!

st.write("Roll one dice and get the result")

num_sides = st.slider("How many sides should your dice have?", min_value=2, max_value=20)

roll = get_roll(num_sides)

st.write("Roll is:", roll)