import streamlit as st
import pandas as pd

df = pd.read_csv("data/weather.csv")

st.title("Weather Data Dashboard")

st.subheader("Temperature Trend")
st.line_chart(df.set_index('date')['temperature'])

st.subheader("Humidity Levels")
st.bar_chart(df.set_index('date')['humidity'])

st.subheader("Raw Data")
st.write(df)