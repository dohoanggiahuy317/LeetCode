import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby(by='class')['student'].size().reset_index()
    # print(courses)
    courses = courses[courses["student"] >= 5]
    return courses[['class']]