import streamlit as st
st.write("Hello☺️! This is a helpful daily schedule to help you be more: Fabulously Encouraging, Lovely, Incredible, Careing, Incomprehendibly Trustworthy, Yummilicious!") 

#output = st.checkbox("Brush your teeth")
#st.write(output)
if "my_stuff" not in st.session_state:
    st.session_state["my_stuff"] = ["Clean Room", "Check Mailbox"]

title = st.text_input("Add your own", "(example, have a Christmas party)")
if st.button("add a thing"):
    st.session_state["my_stuff"].append(title)


for checkbox in st.session_state["my_stuff"]:
    st.checkbox(checkbox)




#st.write("SESSION STATE:")
#st.write(str(st.session_state))


