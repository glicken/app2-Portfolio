import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/nicky.png")

with col2:
    st.title("Nicholas Smith")
    content = ''' Welcome to my work in progress!'''
    st.write(content)

content2 = """These are some of the apps I'm working on right now.  If you'd like to contribute or 
help me out, just send me an email :-)"""
st.write(content2)

