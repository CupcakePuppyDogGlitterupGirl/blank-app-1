import streamlit as st
import random

def get_roll(num_sides, num_dice):
    total = 0 
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        total = total+roll
    
    return total
# HOMEWORK: Make the get_roll function work!

st.write("Roll two dice and get the result")

num_sides = st.slider("How many sides should your dice have?", min_value=2, max_value=20)
num_dice = st.slider("How many dice do you want to roll?")
roll = get_roll(num_sides, num_dice)

st.write("Roll is:", roll)

st.button("Reroll")