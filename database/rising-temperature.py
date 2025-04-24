import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    date = date.sort_values(by="recordDate")
    date = []
    prev = float("INF")

    for index, row in weather.iterrows():
        if row["temperature"] > prev:
            date.append({
                "id": row["id"],
            })

        prev = row["temperature"]
    if date:
        return pd.DataFrame(date)
    else:
        df = pd.DataFrame()
        df["id"] = ""
        return df