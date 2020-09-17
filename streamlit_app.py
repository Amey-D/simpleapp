import time
import random
import streamlit as st
import socket


st.write(f"*** Running on {socket.gethostname()} ***")

@st.cache
def get_random_number():
    return random.randint(0, 1000)

st.title("!! Test App!!!")

file_obj = st.sidebar.file_uploader('Choose an image:', ('jpg', 'jpeg'))

value = st.slider("Pick a number", 0, 10, 3)

st.write(value)

input = st.text_input("Tell me something", "Cantami o Diva")

with open("temp_file.txt", "a") as f:
  f.write(f"{input}\n")
  
with open("temp_file.txt", "r") as f:
  st.write(f.read())

st.write("Streamlit is fabulous")

st.write("Hello Corey, this is the demo!")
st.balloons()
print("this is a log line")
time.sleep(5)
st.write("It's time for some more balloons!")
st.balloons()
st.write("Force pushing an update")
st.write("Force pushing another update")

st.write(f"Your lucky number is: {get_random_number()} !!!")

