import pandas

# Load data from CSV file
data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")

# Group data by 'Primary Fur Color' and count occurrences
relevant_data = data.groupby("Primary Fur Color").size()

# Create a DataFrame with fur color and corresponding counts
df = pandas.DataFrame(
    {"Primary Fur Color": relevant_data.index, "Count": relevant_data.values}
)

# Sort DataFrame by count in descending order
df = df.sort_values(by="Count", ascending=False)

# Reset index of the DataFrame
df = df.reset_index(drop=True)

# Save the sorted data to a new CSV file
df.to_csv("squirrel_count.csv")
