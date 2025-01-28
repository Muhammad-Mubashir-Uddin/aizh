import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("ev_data.csv")
    return df

df = load_data()

# Title
st.title("🚗 EV Charging Station Dashboard - Karachi")

# Data Overview
st.write("## 🔍 Data Overview")
st.dataframe(df.head())

# Vehicle Count by Area
st.write("## 📊 EV Vehicles in Different Areas")
fig = px.bar(df, x="area", y="num_ev", color="area", title="EV Vehicles in Karachi Areas")
st.plotly_chart(fig)

# Interactive Map
st.write("## 🗺️ EV Charging Stations Map")
m = folium.Map(location=[24.8607, 67.0011], zoom_start=12)

# Add Charging Stations to Map
for _, row in df.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=f"Area: {row['area']}\nEV Count: {row['num_ev']}",
        icon=folium.Icon(color="blue", icon="bolt", prefix="fa")
    ).add_to(m)

folium_static(m)
