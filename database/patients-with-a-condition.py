import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    def check(c):
        for each in c.split(" "):
            if each.startswith("DIAB1"):
                return True

        return False

    return patients[patients["conditions"].apply(lambda x: check(x))]