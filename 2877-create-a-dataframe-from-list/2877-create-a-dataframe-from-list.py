import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # Convert the list into dataframe with required column names
    return pd.DataFrame(student_data, columns=["student_id","age"])