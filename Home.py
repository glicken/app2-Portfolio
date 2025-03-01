import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns([1,3])

with col1:
    st.image("images/nicky.png", width=200)

with col2:
    st.title("Nicholas Smith")
    content = ''' Welcome to my work in progress!'''
    st.write(content)

content2 = """These are some of the apps I'm working on right now.  If you'd like to contribute or 
help me out, just send me an email :-)"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
  