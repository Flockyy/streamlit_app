import streamlit as st
import pandas as pd
import time
import numpy as np

st.set_page_config(
    page_title="Plots",
    page_icon="📊",
)

df = pd.read_csv('/Users/fabgrall/Documents/data_engineer/employes_data_test.csv')

st.title("Plots")

st.bar_chart(df, x='affiliate', y='mean_salary', use_container_width=True)
st.bar_chart(df, x='affiliate', y='lowest_salary', use_container_width=True)
st.bar_chart(df, x='affiliate', y='highest_salary', use_container_width=True)