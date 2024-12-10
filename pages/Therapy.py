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
     'songs/emotional-cinematic-inspirational-piano-main-10524.mp3',
     'songs/motivational-music-inspirational-cinematic-background-intro-theme-261168.mp3',
     'songs/ukulele-160363.mp3',
     'songs/inspirational-epic-224660 (1).mp3',
     'songs/inspirational-epic-orchestral-186819 (1).mp3',
     
]
     



st.write("If you want to experience a moment of joy and unforgetable adorability, click the button!!")
    
if st.button("Therapy Generator"):
    

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



st.write("Below are quotes that can encourage and energize people.")
Bible_Quotes, John_Piper, Tim_Keller = st.tabs(["Bible", "John Piper", "Tim Keller"])

with Bible_Quotes:
    st.write("Isaiah 41:10 Fear not, for I am with you; be not dismayed, for I am your God; I will strengthen you, I will help you,I will uphold you with my righteous right hand.")
    st.write("Philippians 4:6-7 Do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be made known to God. And the peace of God, which surpasses all understanding, will guard your hearts and your minds in Christ Jesus.")

with John_Piper:
    st.write("Desire that your life count for something great! Long for your life to have eternal significance. Want this! Don’t coast through life without a passion.")
    st.write("But whatever you do, find the God-centered, Christ-exalting, Bible-saturated passion of your life, and find your way to say it and live for it and die for it. And you will make a difference that lasts. You will not waste your life.")

with Tim_Keller:
     st.write("The gospel says you are simultaneously more sinful and flawed than you ever dared believe, yet more loved and accepted than you ever dared hope.")


st.write("####")

st.write("Below is a video to help strengthen and encourage you!")

st.video("https://www.youtube.com/watch?v=cbOo6lpUdlY",autoplay=True)

st.image("calvin0.jpg")

st.image("calvin0.jpg")

st.write("Here are some great jokes to help you laugh more!")

output = st.button("Comics")
st.write(output)

Comics = [
    st.image("https://static1.cbrimages.com/wordpress/wp-content/uploads/2023/11/calvin-s-mom-lets-him-have-a-cigarette-in-calvin-and-hobbes.jpg?q=70&fit=crop&w=825&dpr=1"),
    st.image("calvin0.jpg"),
    st.image("https://static1.cbrimages.com/wordpress/wp-content/uploads/2023/04/calvin-and-hobbes-days-are-just-packed.jpg?q=70&fit=crop&w=825&dpr=1"),
]


if "page number" not in st.session_state:
     st.session_state["page number"]=0


num = st.session_state["page number"]

st.write(Comics[num % 3])

if st.button("Next button"):
    st.session_state["page number"] = st.session_state["page number"] + 1

st.write("SESSION STATE:")
st.write(str(st.session_state))
