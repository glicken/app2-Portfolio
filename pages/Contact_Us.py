import streamlit as st

st.header("Contact Us")
st.write("If you have any questions or feedback, please feel free to contact us at:")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address:")
    message = st.text_area("Your message:")
    button = st.form_submit_button("Send")
    if button:
        message = message + user_email