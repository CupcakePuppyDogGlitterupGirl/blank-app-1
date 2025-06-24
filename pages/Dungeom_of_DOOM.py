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
st.write("###")

room_number = 1


for room in rooms:
    treasures = ", ".join(room["treasures"])
    monsters = ", ".join(room["monsters"])
    secrets = ", ".join(room["secrets"])
    st.write(f"""Welcome to room number {room_number}, we have all this stuff:

treasures: {treasures}

monsters: {monsters}

secrets: {secrets}

###
""")
    room_number = room_number + 1
    
st.write("### Enjoy your stay!")

st.html("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400..700&family=Pacifico&display=swap" rel="stylesheet">

<style>
h3 {
  font-family: "Dancing Script", cursive !important;
  font-optical-sizing: auto;
  font-weight: 600;
  font-style: normal;
}
</style>

""")