import streamlit as st
import pandas as pd
import numpy as np
import faker

st.set_page_config(
    page_title="Data_gen",
    page_icon="📊",
)

fake = faker.Faker()

st.title("Data Generator")


with st.status("Generating data..."):
    data = [
        { 
        "name": fake.first_name(),
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
    
    # Create 20 different companies
    companies = []  
    for i in range(20):
        companies.append(fake.company())
    # Add 15 to 20 employees to each company
    data = []
    for company in companies:
        for i in range(np.random.randint(15, 50)):
            data.append(
                { 
                "name": fake.first_name(),
                "last_name":  fake.last_name(),
                "job": fake.job(),
                "monthly_salary": np.random.randint(3000, 13000),
                "weekly_hours_worked": np.random.randint(20, 50),
                "contract_hours": np.random.randint(20, 50),
                "hourly_rate": np.random.randint(10, 50),
                "affiliate": company,
            }
        )
    
    df_fake = pd.DataFrame(data)
    st.dataframe(df_fake)
    
    
name = st.selectbox("Seach by name", df_fake['name'].unique())

st.dataframe(df_fake[df_fake['name'] == name])

affiliate = st.selectbox("Seach by affilitate", df_fake['affiliate'].unique())

st.dataframe(df_fake[df_fake['affiliate'] == affiliate])