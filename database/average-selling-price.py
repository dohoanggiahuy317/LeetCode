import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    merg = prices.merge(units_sold, on='product_id', how='left')
    fil = merg[ (merg['start_date'] <= merg['purchase_date']) & (merg['purchase_date'] <= merg['end_date']) ]
    fil['revenue'] = fil["units"] * fil["price"]
    agg = fil.groupby("product_id", as_index=False).agg(
        total_revenue=('revenue', "sum"),
        total_units=("units", "sum")
    )

    agg["average_price"] = (agg['total_revenue'] / agg['total_units']).round(2)
    all_products = prices[['product_id']].drop_duplicates()
    result = (
        all_products
        .merge(agg[['product_id','average_price']], on='product_id', how='left')
        .fillna({'average_price': 0})
    )
    return result[['product_id','average_price']]