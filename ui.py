import streamlit as st
from agent import triage

# Title
st.title("AI Support Ticket Triage")

# Input box
text = st.text_area("Enter Support Ticket")

# Analyze button
if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please enter a support ticket.")
    else:
        result = triage(text)

        st.subheader("Result")
        st.write(result)