import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read Excel file into DataFrame
df = pd.read_excel("./values/1.xlsx")

# Create DataFrame with a column named "省编号"
# Remove this line if the column already exists in the Excel file
df = pd.DataFrame(columns=["省编号"])

# Cleaning steps
mean_data = df["省编号"].mean()
std_data = df["省编号"].std()
c = df["省编号"]

# Replace values outside the range of (mean_data - 3*std_data, mean_data + 3*std_data) with NaN
c[(mean_data + 3*std_data < c) | (mean_data - 3*std_data > c)] = np.nan

# Fill NaN values with the median of the column
c.fillna(c.median(), inplace=True)

# Update the "省编号" column in the original DataFrame
df["省编号"] = c

# Print the cleaned DataFrame
print(df)
