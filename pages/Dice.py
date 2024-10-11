import streamlit as st
import random

def get_grade(test_score):
    if test_score == 100:
        grade = "A+"
    elif test_score >= 90:
        grade = "A"
    elif test_score >= 80:
        grade = "B"
    elif test_score >= 70:
        grade = "C"
    else:
        grade = "F"
    return grade

test_score = st.slider("What is your test score?")

grade = get_grade(test_score)

st.write(grade)

# HOMEWORK: Make the get_roll function work!

st.write("Roll two dice and get the result")

num_sides = st.slider("How many sides should your dice have?", min_value=2, max_value=20)

roll = get_roll(num_sides)

st.write("Roll is:", roll)