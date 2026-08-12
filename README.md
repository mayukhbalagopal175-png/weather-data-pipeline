# Weather Data Pipeline

## Project Overview

This project collects weather data using the OpenWeatherMap API and processes the data using AWS services. The data is stored and analyzed using Snowflake and visualized through a Streamlit dashboard.

## Project Workflow

OpenWeatherMap API
        ↓
AWS Lambda
        ↓
DynamoDB / Amazon S3
        ↓
Snowflake
        ↓
Streamlit Dashboard

## Technologies Used

- Python
- OpenWeatherMap API
- AWS Lambda
- Amazon DynamoDB
- Amazon S3
- Snowflake
- Streamlit
- GitHub

## Weather Analysis

The project analyzes:

- Temperature
- Humidity
- Weather conditions
- Observation time

## Current Dataset Insights

- Number of observations: 11
- Minimum temperature: 28.82°C
- Maximum temperature: 29.65°C
- Average temperature: 29.19°C
- Minimum humidity: 57%
- Maximum humidity: 66%
- Average humidity: 61.91%
- Most frequent condition: Broken Clouds

## Streamlit Dashboard

The dashboard provides:

- Weather summary metrics
- Temperature and humidity trends
- Weather-condition analysis
- Raw weather data
- Key insights

## Purpose

The purpose of this project is to demonstrate a complete cloud-based weather data pipeline and analyze the collected data using Snowflake and Streamlit.
