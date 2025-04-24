import streamlit as st
import pandas as pd
from io import StringIO

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
    

uploaded_file = st.file_uploader("Choose a file", type={"csv", "txt", "json"})
if uploaded_file is not None:

    dataframe = pd.read_csv(uploaded_file)
    st.dataframe(dataframe)
    
