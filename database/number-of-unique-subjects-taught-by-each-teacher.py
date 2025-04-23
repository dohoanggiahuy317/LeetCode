import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher = teacher.groupby(by="teacher_id")["subject_id"].nunique().reset_index(name="cnt")
    # print(teacher)
    return teacher