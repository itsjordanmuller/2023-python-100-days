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

print("\n----- Highest Starting Median Salary -----")
# print(clean_df["Starting Median Salary"].idxmax())
# print(clean_df["Undergraduate Major"].loc[43])
print(clean_df.loc[43])

print("\n----- Highest Mid-Career Median Salary -----")
# print(clean_df["Mid-Career Median Salary"].idxmax())
print(clean_df.loc[8])

print("\n----- Lowest Starting Median Salary -----")
# print(clean_df["Starting Median Salary"].idxmin())
print(clean_df.loc[49])

print("\n----- Lowest Mid-Career Median Salary -----")
# print(clean_df["Mid-Career Median Salary"].idxmin())
print(clean_df.loc[18])

# Lowest Risk - Small Difference Between Lowest & Highest Salaries (10th and 90th Percentile)
spread_col = (
    clean_df["Mid-Career 90th Percentile Salary"]
    - clean_df["Mid-Career 10th Percentile Salary"]
)
clean_df.insert(1, "Spread", spread_col)
clean_df.head()

low_risk = clean_df.sort_values("Spread")
print("\n----- Lowest Risk Majors -----")
print(low_risk[["Undergraduate Major", "Spread"]].head())

# Highest Risk - Large Difference Between Lowest & Highest Salaries (10th and 90th Percentile)
high_risk = clean_df.sort_values("Spread", ascending=False)
print("\n----- Highest Risk Majors -----")
print(high_risk[["Undergraduate Major", "Spread"]].head())

# Count of Majors in Each Category
print(clean_df.groupby("Group").count())
