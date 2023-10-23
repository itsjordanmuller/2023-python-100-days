import pandas as pd

df = pd.read_csv("./data/salaries_by_college_major.csv")

# Peek at Top 5 Rows of Data Frame
print(df.head())

# Check Number of Rows and Columns
print(df.shape)

# Print Index of Column Names
print(df.columns)

# Check for NaN Values
print(df.isna())

# Peek at the Last 5 Rows of Data Frame
print(df.tail())

# Drop Any/All NaN Values from Data
clean_df = df.dropna()
# Show Last 5 Rows of Data Cleared of NaN Values
print(clean_df.tail())

print("----- Highest Starting Median Salary -----")
# print(clean_df["Starting Median Salary"].idxmax())
# print(clean_df["Undergraduate Major"].loc[43])
print(clean_df.loc[43])
