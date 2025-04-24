import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    date = []
    prev = float("INF")

    for index, row in weather.iterrows():
        if row["temperature"] > prev:
            date.append({
                "id": row["id"],
            })

        prev = row["temperature"]

    return pd.DataFrame(date)