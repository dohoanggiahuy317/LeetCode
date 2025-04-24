import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema[(cinema["id"] % 2 == 1) & (cinema["description"]!="boring")][["id", "movie", "description", "rating"]].sort_values(by="rating", ascending=False)