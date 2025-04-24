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
    

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    
