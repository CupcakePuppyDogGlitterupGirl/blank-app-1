# K now it should be pretty simple. We just need to make it do a random verse along with the doggie image and song.
import streamlit as st
import random
st.title("Welcome to Therapy with Felica and Kizzypop!")
st.write("We hope that you can complete the following and become filled with delight and rejuvenation!")
image_urls = [
     'https://hips.hearstapps.com/hmg-prod/images/little-cute-maltipoo-puppy-royalty-free-image-1652926025.jpg',
     'https://upload.wikimedia.org/wikipedia/commons/4/47/American_Eskimo_Dog.jpg',
     'https://upload.wikimedia.org/wikipedia/commons/b/b2/Dog-1123016_960_720.jpg',
     'cutiedoggiegiphy1.gif',
     'mowhawk doggie.jpg',
     'gifdog1.gif',
     'doggif1.gif',
     'cutedoggif1.gif',
     'alliesdreamdog.jpeg',
     'a.jpeg',
     'mydreamdog.jpeg',
     'cuteawwww.jpeg',
     'dogjumplake.gif',
     'jumpindog.gif',
     'lotsdogswater.gif',
     'pullsleddogs.jpeg',
     'pupyrinning.jpeg',
     'swimdoggie.jpeg',
     'swimgolddog.jpeg',
     'tiredpup.jpeg'

]

sound_urls = [
     'songs/epic-emotinal-inspirational-207071.mp3',
     'songs/inspirational-music-motivational-epic-background-intro-theme-259697.mp3',
     'songs/exciting-inspirational-music-motivational-background-intro-theme-269841 (2).mp3',

]

with st.chat_message("user"):
    st.write("If you want to experience a moment of joy and unforgetable adorability, click the button!!")
    
    if st.button("The Button"):
    

          image_pick=random.choice(image_urls)
          st.image(image_pick, width=450)
          sound_pick=random.choice(sound_urls)  
          st.audio(sound_pick, autoplay=True)

with st.expander("Click here to see options for animals up for adoption."):
     st.image("https://static.streamlit.io/examples/dog.jpg")

     

#(222 kB)
#https://hips.hearstapps.com/hmg-prod/images/little-cute-maltipoo-puppy-royalty-free-image-1652926025.jpg

#(661 kB)
#hfttps://upload.wikimedia.org/wikipedia/commons/4/47/American_Eskimo_Dog.jpg

#(213 kB)
#https://upload.wikimedia.org/wikipedia/commons/b/b2/Dog-1123016_960_720.jpg

#(95 kB)
