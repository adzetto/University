import numpy as np
import pandas as pd

# Function to calculate MVP, SD, and SEM
def calculate_statistics(data):
    df = pd.DataFrame(data)
    df['MVP'] = df.iloc[:, 2:].mean(axis=1)
    df['SD'] = df.iloc[:, 2:].std(axis=1, ddof=1)
    df['SEM'] = df['SD'] / np.sqrt(df.shape[1] - 2)  # Assuming 3 measurements, adjust if necessary
    return df

# Data from the tables
data_pace_factor_practice = {
    "From": ["A", "IP1", "IP2", "C", "IP3"],
    "To": ["IP1", "IP2", "B", "IP3", "A"],
    "1st": [30.0000, 30.0000, 23.2800, 30.0000, 12.6400],
    "2nd": [29.7000, 29.6900, 23.2700, 30.0000, 12.6600],
    "3rd": [29.7200, 29.7000, 23.2600, 30.0000, 12.7000],
}

data_pacing = {
    "Person": ["Melih Berke KARAADAM", "Mert BAY", "Mert BOSTANCI", "Mevlut Yagiz KUL", "Muhammet YAGCIOGLU", "Muhammet Taylan ARSLAN"],
    "1st": [109.0000, 112.0000, 109.0000, 112.0000, 102.0000, 114.0000],
    "2nd": [109.0000, 111.0000, 110.0000, 108.0000, 102.0000, 113.0000],
    "3rd": [109.0000, 113.0000, 116.0000, 110.0000, 102.0000, 115.0000],
}

data_indirect_ranging = {
    "From": ["P_1", "IP4", "IP5", "IP6"],
    "To": ["IP4", "IP5", "IP6", "P_2"],
    "1st": [14.7000, 6.6000, 30.0000, 29.6000],
    "2nd": [14.8000, 6.5000, 30.0000, 28.6000],
    "3rd": [14.6000, 6.5000, 30.0000, 29.0000],
}

# Calculating statistics for each dataset
df_pace_factor_practice = calculate_statistics(data_pace_factor_practice)
df_pacing = calculate_statistics(data_pacing)
df_indirect_ranging = calculate_statistics(data_indirect_ranging)