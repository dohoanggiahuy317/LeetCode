import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    mask = (
        (employees["employee_id"] % 2 == 1) & 
        (~employees["name"].str.startswith("M"))
    )

    employees["bonus"] = employees["salary"].where(mask, 0)
    return employees[["employee_id", "bonus"]].sort_values('employee_id')