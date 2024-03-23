import streamlit as st
from openai import OpenAI
import random
import time

#making columns for header components
col1, col2 = st.columns([2,1])

#header 

col1.header("Study Suite AI")
col1.write("Your one stop shop for a tailored study experience")

col2.image(r"studysuitepic.png", width=None)

background_color = "#CEDBDD"
text_color = "#000000"

#about section
st.markdown(
    f"""
    <div style="background-color:{background_color}; text-align: center;">
        <span style="color:{text_color}; font-weight: bold; font-size: 16px;">About Us</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div>
        <span style="color:{text_color}; font-weight: 100; font-size: 16px;">Study Suite AI was founded in March 2024 by Howard University student Heaven Golladay-Watkins. She created this website to help students like her learn more about various subjects. From her hard work, Study Buddy has now helped millions of students around the world understand different concepts.</span>
    </div>
    """,
    unsafe_allow_html=True
)

#how to section
st.markdown(
    f"""
    <div style="background-color:{background_color}; text-align: center;">
        <span style="color:{text_color}; font-weight: bold; font-size: 16px;">How to get started!</span>
    </div>
    """,
    unsafe_allow_html=True
)

    #text
st.write("Select what sort of help you need")
st.write("Specify the subject you want to learn, provide many details and images (if applicable) for the best results")
st.write("Study! Our high-tech AI will respond with a personalized study plan to help you grow as a student")


#select section
    #header
st.markdown(
    f"""
    <div style="background-color:{background_color}; text-align: center;">
        <span style="color:{text_color}; font-weight: bold; font-size: 16px;">Select</span>
    </div>
    """,
    unsafe_allow_html=True
)

    #columns
col3,col4 = st.columns([1,1])

    #robot gif
col3.markdown("![Alt Text](https://i.gifer.com/3q63.gif)")

    #select box
option = col4.selectbox("Select a subject", ["Math", "Science", "English","Foreign Language", "History", "Art"])

#specify section
st.markdown(
    f"""
    <div style="background-color:{background_color}; text-align: center;">
        <span style="color:{text_color}; font-weight: bold; font-size: 16px;">Specify (Chat directly with your AI study buddy!)</span>
    </div>
    """,
    unsafe_allow_html=True
)
    # chat

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})


