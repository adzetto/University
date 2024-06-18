import pandas as pd
import numpy as np
from scipy import stats

data_peg_test = {
    "Measurement": ["Melih Steps", "Initial Staff Readings at Point A", "Initial Staff Readings at Point B"],
    "Description": ["Number of Steps", "Upper (cm)", "Upper (cm)"],
    "Value (cm)": [None, 80.2, 203.5],  # None for steps as it's not directly relevant to calculations here
    "Repeat Measurements (cm)": [None, [80.1, 80.2], [202.5, 202.6]]
}

data_pacing_accuracy = {
    "Measurement": ["Pacing Length", "Pacing Factor"],
    "Value (cm)": [78.466, None],
    "Calculations": [None, 0.7],
    "Average (cm)": [78.466, 0.7]
}

data_stadia_constant = {
    "Distance (m)": [20, 30],
    "Top Hair Reading (cm)": [115.5, 106.5],
    "Bottom Hair Reading (cm)": [95, 75.5],
    "Difference (cm)": [20.5, 31],
    "Stadia Constant (K)": [None, None]  # Placeholder, as it's unclear how to calculate without formula
}

df_peg_test = pd.DataFrame(data_peg_test)
df_pacing_accuracy = pd.DataFrame(data_pacing_accuracy)
df_stadia_constant = pd.DataFrame(data_stadia_constant)

df_stadia_constant['Stadia Constant (K)'] = df_stadia_constant['Difference (cm)'] / df_stadia_constant['Distance (m)']

combined_df = df_stadia_constant

mean_k = combined_df['Stadia Constant (K)'].mean()
print(f"Mean K Value: {mean_k}")

confidence_level = 0.95
degrees_freedom = len(combined_df['Stadia Constant (K)']) - 1
standard_error = stats.sem(combined_df['Stadia Constant (K)'].dropna())

confidence_interval = stats.t.interval(confidence_level, degrees_freedom, mean_k, standard_error)
print(f"Confidence Interval for K Value: {confidence_interval}")

latex_code = combined_df.to_latex(index=False, caption="Combined Data for Stadia Method Calculations", label="table:combined_stadia", longtable=True, column_format="lcccc", header=["Distance (m)", "Top Hair Reading (cm)", "Bottom Hair Reading (cm)", "Difference (cm)", "Stadia Constant (K)"])

print(latex_code)