import pandas

FILEPATH = "https://corgis-edu.github.io/corgis/datasets/csv/airlines/airlines.csv"

df = pandas.read_csv(FILEPATH)

rows, columns = df.shape

print(columns)

new_column = (
    df["Statistics.# of Delays.National Aviation System"]
    .add(df["Statistics.# of Delays.Carrier"])
    .add(df["Statistics.# of Delays.Late Aircraft"])
    .add(df["Statistics.# of Delays.Security"])
    .add(df["Statistics.# of Delays.Weather"])
)

df.insert(columns, "SumDelays", new_column, True)

df["Time.Label"] = pandas.to_datetime(df["Time.Label"])

all_one_months = df["Time.Label"].dt.month == 1

print(
    df[["Airport.Code", "Airport.Name", "Time.Label"]][
        (df["Time.Label"].dt.month == 1) & (df["SumDelays"] == df["SumDelays"].max())
    ]
)
