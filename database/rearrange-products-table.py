import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    
    final = []

    for index, row in products.iterrows():
        product_id = row['product_id']

        for store in ['store1', 'store2', 'store3']:
            price = row[store]
            if pd.notnull(price):
                final.append({
                    'product_id': product_id,
                    'store': store,
                    'price': price
                })

    return pd.DataFrame(final)