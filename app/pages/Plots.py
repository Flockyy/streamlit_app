import streamlit as st
import pandas as pd
import time
import numpy as np
import faker

fake = faker.Faker()

st.set_page_config(
    page_title="Plots",
    page_icon="📊",
)
data = [
             { "nom": fake.first_name(),
               "last_name":  fake.last_name(),
               "job": fake.job(),
               "monthly_salary": np.random.randint(3000, 13000),
               "weekly_hours_worked": np.random.randint(20, 50),
                "contract_hours": np.random.randint(20, 50),
                "hourly_rate": np.random.randint(10, 50),
                "affiliate": fake.company(),
             }
             for i in range(100000)
         ]
df_fake = pd.DataFrame(data)
st.dataframe(df_fake)

df = pd.read_csv('app/data/employes_data_test.csv')

st.title("Plots")

st.bar_chart(df, x='affiliate', y='mean_salary', use_container_width=True)
st.bar_chart(df, x='affiliate', y='lowest_salary', use_container_width=True)
st.bar_chart(df, x='affiliate', y='highest_salary', use_container_width=True)

st.altair_chart(df, x='affiliate', y='mean_salary', use_container_width=True)