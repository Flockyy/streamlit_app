import streamlit as st
import pandas as pd
import numpy as np
import faker

st.set_page_config(
    page_title="Data_gen",
    page_icon="📊",
)

fake = faker.Faker()


data = [
    { 
    "nom": fake.first_name(),
    "last_name":  fake.last_name(),
    "job": fake.job(),
    "monthly_salary": np.random.randint(3000, 13000),
    "weekly_hours_worked": np.random.randint(20, 50),
    "contract_hours": np.random.randint(20, 50),
    "hourly_rate": np.random.randint(10, 50),
    "affiliate": fake.company(),
}
    for i in range(1000)
]

df_fake = pd.DataFrame(data)
st.dataframe(df_fake)