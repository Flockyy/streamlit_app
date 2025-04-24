import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="main",
    page_icon="👋",
)

st.sidebar.success("Select a demo above.")

st.title("Hello Streamlit-er 👋")

df = pd.read_csv('app/data/employes_data_test.csv')
st.dataframe(df)

name = st.selectbox("Seach by name", df['name'].unique())

st.dataframe(df[df['name'] == name])

affiliate = st.selectbox("Seach by affilitate", df['affiliate'].unique())

st.dataframe(df[df['affiliate'] == affiliate])

if st.button("Send balloons!"):
    st.balloons()
    

uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)