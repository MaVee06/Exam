import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ETH Ward Elections",
    page_icon="🗳️",
    layout="wide"
)

st.title("🗳️ ETH Ward Elections Dashboard")

st.write("Welcome to the ETH Ward Elections dashboard.")

# Load data
df = pd.read_csv("ETH_Ward.csv")

st.subheader("Election Data")

st.dataframe(df, use_container_width=True)

st.subheader("Basic Statistics")

st.write(df.describe())
