import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby(by='customer_number')['order_number'].size().reset_index()
    orders.sort_values(by="order_number", ascending=False, inplace=True)
    return orders[['customer_number']].head(1)