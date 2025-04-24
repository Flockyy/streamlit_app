import streamlit as st
import pandas as pd
from io import StringIO
from faker import Faker

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

uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)

# let's create a function to check the file types and read them accordingly.

def extract(file_to_extract):
    if file_to_extract.name.split(".")[-1] == "csv": 
        extracted_data = pd.read_csv(file_to_extract)

    elif file_to_extract.name.split(".")[-1] == 'json':
        extracted_data = pd.read_json(file_to_extract, lines=True)

    elif file_to_extract.name.split(".")[-1] == 'xml':
        extracted_data = pd.read_xml(file_to_extract)
         
    return extracted_data

# create an empty list which will be used to merge the files.

dataframes = []
    
if uploaded_files:
    for file in uploaded_files:
        file.seek(0)
        df = extract(file)
        dataframes.append(df)

    if len(dataframes) >= 1:
        merged_df = pd.concat(dataframes, ignore_index=True, join='outer')

    remove_duplicates = st.selectbox("Remove duplicate values ?", ["No", "Yes"])
    remove_nulls = st.selectbox("Remove null values in the dataset ?", ["Yes", "No"])

    if remove_duplicates == "Yes":
        merged_df.drop_duplicates(inplace=True)

    if remove_nulls == "Yes":
        merged_df.dropna(how="all", inplace=True)

    
    show_result = st.checkbox("Show Result", value=True)

    if show_result:
        st.write(merged_df)

    csv = merged_df.to_csv().encode("utf-8")

    st.download_button(label="Download cleaned data as csv",
                       data=csv,
                       file_name="cleaned_data.csv",
                       mime="text/csv")