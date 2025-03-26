import streamlit as st
import os

FILE_PATH = "data.txt"

# Function to load text from file
def load_text():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            return f.read()
    return ""

# Function to save text to file
def save_text(content):
    with open(FILE_PATH, "w") as f:
        f.write(content)

# Streamlit UI
st.title("Collaborative Text Pad")

text = st.text_area("Edit text here:", load_text(), height=300)

if st.button("Save Text"):
    save_text(text)
    st.success("Text saved! Others will see it on refresh.")

st.button("Refresh", on_click=st.experimental_rerun)
