import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    no_orders = ~customers["id"].isin(orders["customerId"])
    df = customers.loc[no_orders, ['name']]
    df.rename(columns={"name": "Customers"}, inplace=True)
    return df