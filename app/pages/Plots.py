import streamlit as st
import pandas as pd

df = pd.read_csv('app/data/employes_data_test.csv')

st.title("Plots")

st.bar_chart(df, x='affiliate', y='mean_salary', use_container_width=True)
st.bar_chart(df, x='affiliate', y='lowest_salary', use_container_width=True)
st.bar_chart(df, x='affiliate', y='highest_salary', use_container_width=True)

st.altair_chart(df, x='affiliate', y='mean_salary', use_container_width=True)