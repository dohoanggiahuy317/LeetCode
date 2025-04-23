import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates(subset=['sell_date', "product"])
    activities = activities.groupby(by="sell_date").agg(
        num_sold=('product', 'nunique'),
        products=('product', lambda x: ",".join(sorted(x)))
    ).reset_index().sort_values('sell_date').reset_index(drop=True)
    # print(activities)
    return activities