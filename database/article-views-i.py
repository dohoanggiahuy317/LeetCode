import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    same_views = views[views["author_id"] == views["viewer_id"]][["author_id"]]
    same_views.rename(columns={"author_id": "id"}, inplace = True)
    same_views.drop_duplicates(inplace=True)
    same_views.sort_values(by="id", inplace = True)

    return same_views