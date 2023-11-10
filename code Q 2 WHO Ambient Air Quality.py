# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 22:18:34 2023

@author: arbab
"""

import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_excel(file_path)

def pie_plot(data, country):
    country_data = data[data['Country'] == country]
    
    if not country_data.empty:
        values = country_data.iloc[:, 1:].values.flatten()  # Flatten the 2D array to 1D
        labels = data.columns[1:].repeat(len(country_data))  # Repeat labels for each value
        
        plt.figure(figsize=(8, 8))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(f'Ambient Air Quality Distribution in {country}')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()
    else:
        print(f'No data found for {country}.')

# Load data from Excel file
file_path = 'C:\\Program Files\\Spyder\\pkgs\\pandas\\io\\Q 2 WHO Ambient Air Quality.xlsx'  # Replace with the actual file path
df_air_quality = load_data(file_path)

# Choose a specific country for visualization
selected_country = 'Pakistan'

# Plot pie chart for the selected country
pie_plot(df_air_quality, selected_country)


