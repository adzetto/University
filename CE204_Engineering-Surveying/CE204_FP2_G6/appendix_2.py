import numpy as np
from scipy.stats import sem

measurements = {
    'P3-P5': [70.17, 69.70, 69.20, 68.27, 69.40, 70.56, 20.40, 67.50, 69.80],
    'P2-P5': [69.21, 67.40, 66.48, 67.18, 66.93, 64.85, 66.22, 67.841, 69.41],
    'P1-B3': [33.64, 30.70, 20.69],
    'P4-B1': [21.32, 26.30, 27.753],
    'P3-B2': [40.33, 50.79, 52.78],
}

def calculate_statistics(data):
    mpv = np.mean(data)
    sd = np.std(data, ddof=1)
    sem_val = sem(data, ddof=1)
    return mpv, sd, sem_val

results = []

for side, data in measurements.items():
    mpv, sd, sem_val = calculate_statistics(data)
    results.append([side, mpv, sd, sem_val])

distances = [result[1] for result in results]
sds = [result[2] for result in results]

total_distance = np.sum(distances)
propagated_error = np.sqrt(np.sum(np.array(sds) ** 2))

results.append(["Total", total_distance, "-", propagated_error])

from tabulate import tabulate
headers = ["Side", "MPV (m)", "SD (m)", "SEM (m)"]
table = tabulate(results, headers=headers, tablefmt="latex_booktabs")
print(table)


# Assumed MPV values for the sides
mpv_values = {
    'P5P3': 63.8889,  # Example MPV for P5P3
    'P4B1': 25.1243,  # Example MPV for P4B1
    'P5P2': 67.2801,  # Example MPV for P5P2
    'P1B3': 28.3433,  # Example MPV for P1B3
    'P3B2': 47.9667   # Example MPV for P3B2
}

areas = {    'Triangle1 (P5P3-P4B1)': 0.5 * mpv_values['P5P3'] * mpv_values['P4B1'],
    'Triangle2 (P5P2-P1B3)': 0.5 * mpv_values['P5P2'] * mpv_values['P1B3'],
    'Triangle3 (P5P2-P3B2)': 0.5 * mpv_values['P5P2'] * mpv_values['P3B2']
}

for triangle, area in areas.items():
    print(f"Area of {triangle}: {area:.2f} square units")
