import streamlit as st
from snowflake.snowpark.context import get_active_session

# Get Snowflake session
session = get_active_session()

# Page configuration
st.set_page_config(
    page_title="Bangalore Weather Dashboard",
    page_icon="🌦️",
    layout="wide"
)

# Title
st.title("🌦️ Bangalore Weather Analysis Dashboard")

st.write(
    "Weather data collected using OpenWeatherMap API "
    "and stored in Snowflake."
)

# Get weather data from Snowflake
df = session.sql("""
    SELECT
        OBSERVATION_TIME,
        TEMPERATURE,
        HUMIDITY,
        WEATHER
    FROM WEATHER_DB.PUBLIC.WEATHER_DATA
""").to_pandas()

# Calculate metrics
min_temp = df["TEMPERATURE"].min()
max_temp = df["TEMPERATURE"].max()
avg_temp = df["TEMPERATURE"].mean()
avg_humidity = df["HUMIDITY"].mean()
min_humidity = df["HUMIDITY"].min()
max_humidity = df["HUMIDITY"].max()

# Display metrics
st.subheader("📊 Weather Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🌡️ Minimum Temperature", f"{min_temp:.2f} °C")

with col2:
    st.metric("🌡️ Maximum Temperature", f"{max_temp:.2f} °C")

with col3:
    st.metric("🌡️ Average Temperature", f"{avg_temp:.2f} °C")

with col4:
    st.metric("💧 Average Humidity", f"{avg_humidity:.2f} %")

st.subheader("💧 Humidity Range")

col1, col2 = st.columns(2)

with col1:
    st.metric("Minimum Humidity", f"{min_humidity:.0f}%")

with col2:
    st.metric("Maximum Humidity", f"{max_humidity:.0f}%")

# Weather condition analysisst.subheader("💧 Humidity Range")

col1, col2 = st.columns(2)

with col1:
    st.metric("Minimum Humidity", f"{min_humidity:.0f}%")

with col2:
    st.metric("Maximum Humidity", f"{max_humidity:.0f}%")
st.subheader("☁️ Weather Conditions")

weather_counts = df["WEATHER"].value_counts()

st.bar_chart(weather_counts)

# Show data
st.subheader("📋 Weather Data")

st.dataframe(df, use_container_width=True)

# Temperature and Humidity Trend
st.subheader("📈 Temperature & Humidity Trend")

chart_data = df[["OBSERVATION_TIME", "TEMPERATURE", "HUMIDITY"]].copy()

chart_data = chart_data.set_index("OBSERVATION_TIME")

st.line_chart(chart_data)

# Key Insights

st.subheader("💡 Key Insights")

st.write(
    f"🌡️ Temperature ranged from {min_temp:.2f}°C to {max_temp:.2f}°C."
)

st.write(
    f"💧 Humidity ranged from {min_humidity:.0f}% to {max_humidity:.0f}%, "
    f"with an average of {avg_humidity:.2f}%."
)

most_common_weather = df["WEATHER"].value_counts().idxmax()
most_common_count = df["WEATHER"].value_counts().max()

st.write(
    f"☁️ {most_common_weather.title()} was the most frequently recorded "
    f"weather condition ({most_common_count} observations)."
)