import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="main",
    page_icon="👋",
)

st.sidebar.success("Select a demo above.")

st.title("Hello Streamlit-er 👋")
st.markdown(
    """ 
    This is a playground for you to try Streamlit and have fun. 

    **There's :rainbow[so much] you can build!**
    
    We prepared a few examples for you to get started. Just 
    click on the buttons above and discover what you can do 
    with Streamlit. 
    """
)

df = pd.read_csv('/Users/fabgrall/Documents/data_engineer/employes_data_test.csv')
st.dataframe(df)

name = st.selectbox("Seach by name", df['name'].unique())

st.dataframe(df[df['name'] == name])

affiliate = st.selectbox("Seach by affilitate", df['affiliate'].unique())

st.dataframe(df[df['affiliate'] == affiliate])

if st.button("Send balloons!"):
    st.balloons()