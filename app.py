import streamlit as st
import datetime

st.set_page_config(page_title="Kingsley's First App", page_icon="🚀")

st.title("Welcome to My First Web App!")
st.write("I built this with Python only!")

st.subheader(f"Built by Kingsley 🎉")

name = st.text_input("What's your name?")
if name:
    st.success(f"Hello {name}! Welcome to my app.")

date = st.date_input("Pick a date", datetime.date.today())
st.write(f"You selected: {date}")

if st.button("Click me for a surprise"):
    st.balloons()