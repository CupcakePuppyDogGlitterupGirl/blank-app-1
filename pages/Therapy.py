import streamlit as st
import random
st.title("Welcome to Therapy with Felica and Kate!")
st.write("We hope that you can complete the following and become filled with joy and become rejuvenated!")
image_urls = [
     ('https://hips.hearstapps.com/hmg-prod/images/little-cute-maltipoo-puppy-royalty-free-image-1652926025.jpg'),
     ('https://upload.wikimedia.org/wikipedia/commons/4/47/American_Eskimo_Dog.jpg'),
     ('https://upload.wikimedia.org/wikipedia/commons/b/b2/Dog-1123016_960_720.jpg')
]
with st.chat_message("user"):
    st.write("If you want to experience a moment of joy click the button and see some amazing dog pictures!!")
    st.button("Reset", type="primary")
    st.link_button("show dog Photo 1:", image_urls[0])
    st.link_button("show dog Photo 2:", image_urls[1])
    st.link_button("show dog Photo 3:", image_urls[-1])
with st.expander("Click here to see options for animals up for adoption."):
     st.image("https://static.streamlit.io/examples/dog.jpg")
image_pick=random.choice(image_urls)
st.image(image_pick)
     

#(222 kB)
#https://hips.hearstapps.com/hmg-prod/images/little-cute-maltipoo-puppy-royalty-free-image-1652926025.jpg

#(661 kB)
#hfttps://upload.wikimedia.org/wikipedia/commons/4/47/American_Eskimo_Dog.jpg

#(213 kB)
#https://upload.wikimedia.org/wikipedia/commons/b/b2/Dog-1123016_960_720.jpg

#(95 kB)
