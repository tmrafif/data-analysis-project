# E-Commerce Public Data Analysis with Python - Dicoding

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)

## Overview
This project is a data analysis and visualization project focused on e-commerce public data. It includes code for data wrangling, exploratory data analysis (EDA), and a Streamlit dashboard for interactive data exploration. This project aims to analyze data on the E-Commerce Public Dataset.

## Project Structure
- `/dashboard`: Directory containing dashboard.py which is used to create dashboards of data analysis results.
- `/data`: Directory containing the raw CSV data files.
- `data_analysis_project.ipynb`: File used to perform data analysis.
- `README.md`: This documentation file.

## Installation
1. Clone this repository to your local machine:
```
git clone https://github.com/tmrafif/data-analysis-project-dicoding.git
```
2. Go to the project directory
```
cd data-analysis-project-dicoding
```
3. Install the required Python packages by running:
```
pip install -r requirements.txt
```

## Usage
1. **Data Wrangling**: Data wrangling scripts are available in the `data_analysis_project.ipynb` file to prepare and clean the data.

2. **Exploratory Data Analysis (EDA)**: Explore and analyze the data using the provided Python scripts. EDA insights can guide your understanding of e-commerce public data patterns.

3. **Visualization**: Run the Streamlit dashboard for interactive data exploration:

```
cd data-analyst-dicoding/dashboard
streamlit run dashboard.py
```
Access the dashboard in your web browser at `http://localhost:8501` or you can visit this website [E-Commerce Dashboard Streamlit App](https://tmrafif-project-data-analytics.streamlit.app/)

## Data Sources
The project uses [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) from [Kaggle](https://www.kaggle.com/).