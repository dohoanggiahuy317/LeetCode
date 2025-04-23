import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity[["player_id", "event_date"]]
    activity = activity.sort_values(by="event_date", inplace=False)
    activity = activity.drop_duplicates(subset="player_id", keep="first", inplace=False)
    activity = activity.rename(columns={
        "event_date": "first_login"
    }, inplace=False)
    return activity