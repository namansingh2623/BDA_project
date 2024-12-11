import pandas as pd
import matplotlib.pyplot as plt
import dataprocessing as dp

# Load data
dataframes = dp.process_and_clean_data()

pre_occup_df = dataframes['occupation_11_1929']
post_occup_df = dataframes['occupation_11_2333']

# Normalize column names for consistency
pre_occup_df["2019 National Employment Matrix title"] = pre_occup_df["2019 National Employment Matrix title"].str.strip().str.lower()
post_occup_df["2023 National Employment Matrix title"] = post_occup_df["2023 National Employment Matrix title"].str.strip().str.lower()

# Merge dataframes on occupation title
merged_df = pd.merge(
    pre_occup_df[["2019 National Employment Matrix title", "Median annual wage, 2020(1)"]].rename(columns={"Median annual wage, 2020(1)": "2019 Median Wage"}),
    post_occup_df[["2023 National Employment Matrix title", "Median annual wage, dollars, 2023[1]"]].rename(columns={"Median annual wage, dollars, 2023[1]": "2023 Median Wage"}),
    left_on="2019 National Employment Matrix title",
    right_on="2023 National Employment Matrix title",
    how="inner"
)

# Adjust 2019 wages for inflation
inflation_factor = 1.2  # Example inflation factor (adjust based on actual CPI values)
merged_df["2019 Real Wage (2023 $)"] = merged_df["2019 Median Wage"] * inflation_factor

# Extract data for the plot
occupations = merged_df["2019 National Employment Matrix title"].str.title()
real_wages_2019 = merged_df["2019 Real Wage (2023 $)"]
wages_2023 = merged_df["2023 Median Wage"]

# Plot bar graph
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.4
x = range(len(occupations))

# Bars for inflation-adjusted 2019 wages and 2023 wages
ax.bar(x, real_wages_2019, width=bar_width, label="2019 Median Wage (2023 $)", color="skyblue")
ax.bar([i + bar_width for i in x], wages_2023, width=bar_width, label="2023 Median Wage", color="lightcoral")

# Add labels and title
ax.set_xlabel("Occupations", fontsize=12)
ax.set_ylabel("Median Annual Wage (Inflation-Adjusted $)", fontsize=12)
ax.set_title("Comparison of Inflation-Adjusted Median Annual Wages (2019 vs 2023)", fontsize=14)
ax.set_xticks([i + bar_width / 2 for i in x])
ax.set_xticklabels(occupations, rotation=90, fontsize=10)
ax.legend()

# Adjust layout
plt.tight_layout()
plt.show()
