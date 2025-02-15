import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/nicky.png")

with col2:
    st.title("Nicholas Smith")
    content = ''' Welcome to my work in progress!'''
    st.write(content)
