# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 23:15:27 2023

@author: arbab
"""

import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load data from an Excel file into a Pandas DataFrame.

    Parameters:
    - file_path (str): The path to the Excel file.

    Returns:
    - pd.DataFrame: The loaded data.
    """
    return pd.read_excel(file_path)

def bar_plot(data, countries):
    """
    Generate a stacked bar plot for the number of international tourists visiting Thailand (2016-2022).

    Parameters:
    - data (pd.DataFrame): DataFrame containing tourist data with columns 'Year' and countries.
    - countries (list): List of specific countries to include in the visualization.

    Returns:
    - None
    """
    plt.figure(figsize=(10, 6))
    data[countries].plot(kind='bar', stacked=True)
    plt.title('International Tourists Visiting Thailand (2016-2022)')
    plt.xlabel('Year')
    plt.ylabel('Number of Tourists (in thousands)')
    plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

# Load data from Excel file
file_path = 'C:\\Program Files\\Spyder\\pkgs\\pandas\\io\\Q 3 International Tourists Visiting Thailand (2016-2022).xlsx'  # Replace with the actual file path
df_tourists = load_data(file_path)

# Choose specific countries for visualization
selected_countries = ['US', 'UK', 'Canada', 'Australia', 'Dubai']

# Plot bar chart
bar_plot(df_tourists, selected_countries)

