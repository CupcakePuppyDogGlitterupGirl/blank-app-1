import streamlit as st
import random

def get_roll(num_sides):
    roll = random.randint(1, num_sides)
    roll2 = random.randint(1, num_sides)
    return roll2 + roll
# HOMEWORK: Make the get_roll function work!

st.write("Roll two dice and get the result")

num_sides = st.slider("How many sides should your dice have?", min_value=2, max_value=20)

roll = get_roll(num_sides)

st.write("Roll is:", roll)

