import streamlit as st

import streamlit as st

rooms = [
    {
        "treasures": ["birthday cake", "balloons"],
        "monsters": ["adorable teddy bear"],
        "secrets": ["we're planning a surprise party for Mr. Snuggly!"],
    },
    {
        "treasures": ["silver coin"],
        "monsters": ["A little spider"],
        "secrets": ["Don't worry, he's a nice spider!"],
    },
    {
        "treasures": ["Magic Bubbles!! OOoooo!"],
        "monsters": ["Fairies"],
        "secrets": ["The fairies blow a new bubble every time someone runs over a poor squirrel on the road"],
    },
    {
        "treasures": ["an ice cream castle!!"],
        "monsters": ["The live gumdrop!"],
        "secrets": ["The Live gumdrop is BROTHERS with King Candy!!"],
    },
    {
        "treasures": ["emerald"],
        "monsters": ["unicorn", "Agnes Gru"],
        "secrets": ["unicorns are afraid of the dark unless Agnes telles them a bedtime story!"],
    },
    {
        "treasures": ["A perfectly golden-brown marshmallow! mmm!"],
        "monsters": ["A super-cook"],
        "secrets": ["a super-cook never tells his sectet for perfect marshmallows!"],
    },
    {
        "treasures": ["opal", "ruby"],
        "monsters": ["Queen Diamond Twinkle"],
        "secrets": ["the queen's favorite color is glitter!"],
    },
]

st.title("Welcome to the Dungeon of Doom!!! 👹 😎 🥳")
st.write("### An Easy Vacation guide of this spooky tourist atraction!")
room_number = 1
for room in rooms:
    treasures = ", ".join(room["treasures"])
    st.write(f"room number {room_number} has these treasures: {treasures}")
    room_number = room_number + 1
    
for room in rooms:
    monsters = ", ".join(room["monsters"])
    st.write(f"room number {room_number} has these monsters: {monsters}")
    room_number = room_number + 1

for room in rooms:
    secrets = ", ".join(room["secrets"])
    st.write(f"room number {room_number} has these secrets: {secrets}")
    room_number = room_number + 1
st.write("Print out the first room:")
room = rooms[0]
st.write(room)

st.write("Print out the 2nd room:")
room = rooms[1]
st.write(room)


st.write("Print out the last room:")
room = rooms[-1]
st.write(room)

st.write("Print out the treasures in the 2nd room:")
rooms[1]["treasures"]
st.write("Print out the monsters in the 4th room:")
rooms[3]["monsters"]
st.write("Print out the second secret in the 6th room:")
rooms[5]["secrets"]


























































































