import streamlit as st

st.title("Felicity's Magnificent Calculator")

num1 = st.number_input("num1", value=4)

num2 = st.number_input("num2", value=5)


st.button("Reset", type="primary")
if st.button("add"):
    st.write("num1 + num2 =", num1+num2)
if st.button("Multiply"):
    st.write("num1 * num2 =", num1*num2)

if st.button("minus"):
    st.write("num1 - num2 =", num1-num2)
if st.button("Divideeeeeeee"):
    st.write("num1 / num2 =", num1/num2)
    st.balloons()
    