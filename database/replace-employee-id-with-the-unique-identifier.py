import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merge = employees.merge(employee_uni, on="id", how="left")
    return merge[["unique_id", "name"]]