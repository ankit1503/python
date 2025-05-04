import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel_count = len(data[data["Primary Fur Color"]=="Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"]=="Black"])

dict = {"Fur color": ["gray", "Red", "Black"],"count":[gray_squirrel_count, red_squirrel_count, black_squirrel_count]}

df = pandas.DataFrame(dict)
df.to_csv("Fur_color_counts.csv")
print(df)