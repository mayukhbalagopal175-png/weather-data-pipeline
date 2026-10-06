# 🌦️ Kochi Weather Data Pipeline

## 📌 Project Overview

This project is a cloud-based weather data pipeline that collects weather information for **Kochi, Kerala, India** using the OpenWeatherMap API.

The collected weather data is processed and stored using AWS services and Snowflake. The data is then visualized through a Streamlit dashboard for analysis.

---

## 🎯 Project Objective

The main objective of this project is to build an automated weather data pipeline that can:

- Collect weather data from the OpenWeatherMap API
- Process weather data using AWS Lambda
- Store weather information in Amazon DynamoDB
- Store JSON weather files in Amazon S3
- Load the data into Snowflake
- Automatically ingest new data using Snowpipe
- Analyze and visualize the weather data using Streamlit

---

## 🔄 Data Pipeline Architecture

```text
OpenWeatherMap API
        ↓
AWS Lambda
        ↓
Amazon DynamoDB
        ↓
Amazon S3
        ↓
Snowflake External Stage
        ↓
Snowpipe
        ↓
Snowflake WEATHER_DATA Table
        ↓
Streamlit Dashboard
