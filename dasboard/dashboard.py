import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

df = pd.read_csv("cleaned_day.csv", parse_dates=["date"])

st.sidebar.title("Filter Options")
selected_years = st.sidebar.multiselect("Select Year", options=sorted(df['year'].unique()), default=sorted(df['year'].unique()))
selected_seasons = st.sidebar.multiselect("Select Season", options=df['season'].unique(), default=df['season'].unique())

filtered_df = df[df['year'].isin(selected_years) & df['season'].isin(selected_seasons)]

st.title("🚴 Bike Sharing Data Dashboard")

st.subheader("1. Bike Rental Trends by Season and Year")
season_year_group = filtered_df.groupby(['year', 'season'])['total_riders'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=season_year_group, x="season", y="total_riders", hue="year", palette=["#32CD32", "#FFD700"], ax=ax)
ax.set_title("Seasonal Bike Rental Trends per Year")
ax.set_ylabel("Total Rentals")
for container in ax.containers:
    ax.bar_label(container, fmt="%.0f", fontsize=10, color='black')
st.pyplot(fig)

# SECTION 2: Weather Condition Relationship
st.subheader("2. Relationship Between Weather and Bike Rentals")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Temperature vs Rentals**")
    fig1, ax1 = plt.subplots()
    sns.scatterplot(data=filtered_df, x='temperature', y='total_riders', color='green', ax=ax1)
    st.pyplot(fig1)

with col2:
    st.write("**Humidity vs Rentals**")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=filtered_df, x='humidity', y='total_riders', color='blue', ax=ax2)
    st.pyplot(fig2)

with col3:
    st.write("**Windspeed vs Rentals**")
    fig3, ax3 = plt.subplots()
    sns.scatterplot(data=filtered_df, x='windspeed', y='total_riders', color='orange', ax=ax3)
    st.pyplot(fig3)

st.subheader("3. Correlation Heatmap")
correlation_cols = ['temperature', 'apparent_temperature', 'humidity', 'windspeed', 'total_riders']
corr_matrix = filtered_df[correlation_cols].corr()
fig4, ax4 = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=1, linecolor='black', ax=ax4)
ax4.set_title("Correlation between Weather Variables and Bike Rentals")
st.pyplot(fig4)

st.markdown("---")
st.markdown("**Project By: Febriyadi**  |  Cohort: mc323d5y0358@student.devacademy.id  |  Dicoding: febriyadibangkit@gmail.com")
