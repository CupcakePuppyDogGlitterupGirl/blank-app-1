import streamlit as st
import datetime

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

start_date = datetime.date(2000, 1, 1)
end_date = datetime.date(2020, 12, 31)
birthday = st.date_input("When is your birthday?", min_value=start_date, max_value=end_date)


picture = st.camera_input("Take a picture")

sports = st.multiselect(
    "What sports have you played?",
    ["⚽️ soccer", "🏀 basketball", "🏈 football", "⚾️ baseball", "🎾 tennis", "🏐 volley-ball", "🏉 rugby",
    "🏓 ping-pong", "🏒 hockey", "🏏 cricket" ,"🛹 skate-boarding" ,"🛼 rollar-skating" ,"🛷 sleding", "⛸️ ice-skating", "⛷️ skiing", "🥊 boxing" ,"🥋 karate", "🪂 parachuting", "🤸‍♀️ gymnastics" ,"🏄🏻‍♀️ surfing", "🏇 horseback-riding",
    "🏊🏻 swimming" ,"🩰 ballet" ,"🚣🏻‍♀️ rowing", "🧗‍♀️ rock-climbing" ,"🚴🏻‍♂️ biking" ,"🤹‍♀️ juggling"],
)
color = st.color_picker("Fav Color")

visit = st.checkbox("Have you been on the official school visit?")

moodeng = st.checkbox("Do you think Moo Deng is ADORABLE:")




# EXAMPLE OUTPUT
st.subheader("Student info")
st.write("Full name:", full_name)
st.write("Age:", age)
st.write("Birthday:", birthday)
if picture:
    st.image(picture, width=100)
st.write("Sports:\n\n", "\n\n".join(sports))
st.write("Favorite Color:", color)
st.color_picker("Your Favorite Color:", value = color, disabled = True)
st.write("Have been on the school visit:",visit)
st.write("Loves Moo Deng:", moodeng)
if moodeng == True:
    st.write(":rainbow[Hip Hippo Horay!]🦛😍🎉")
else:
    st.write(":red[How DARE you!!]🤯😱")
