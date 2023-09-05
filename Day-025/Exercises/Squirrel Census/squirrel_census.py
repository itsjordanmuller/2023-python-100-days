import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
# print(data)

relevant_data = data.groupby("Primary Fur Color").size()

df = pandas.DataFrame(
    {"Primary Fur Color": relevant_data.index, "Count": relevant_data.values}
)

df = df.sort_values(by="Count", ascending=False)

df = df.reset_index(drop=True)

df.to_csv("squirrel_count.csv")
