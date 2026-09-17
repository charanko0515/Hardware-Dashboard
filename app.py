import streamlit as st

st.title("Hardware Dashboard")
st.divider()
st.text("Welcome to the Hardware Dashboard! Here you can monitor and manage your hardware components.")
st.caption("values only for demonstration purposes")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="CPU Usage", value="45%", delta="-5%")
with col2:
    st.metric(label="RAM Usage", value="70%", delta="-10%")
with col3:
    st.metric(label="GPU Usage", value="20%", delta="-45%")
with col4:
    st.metric(label="DISK Usage", value="99%", delta="+80%")