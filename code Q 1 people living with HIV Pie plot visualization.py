# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:42:20 2023

@author: arbab
"""

import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_excel(file_path)

def line_plot_hiv_estimates(df):
    plt.figure(figsize=(12, 8))

    for country in df['Country']:
        plt.plot(df.columns[1:], df[df['Country'] == country].values.flatten()[1:], label=country)

    plt.title('Estimated Number of People Living with HIV (2017-2022)')
    plt.xlabel('Year')
    plt.ylabel('Estimated Number of People')
    plt.legend()
    plt.grid(True)
    plt.show()

# Replace 'your_file_path.xlsx' with the actual path to your Excel file
file_path = 'C:\Program Files\Spyder\pkgs\pandas\io\Q 1 people living with HIV Pie plot visualization.xlsx'
df = load_data(file_path)
line_plot_hiv_estimates(df)
