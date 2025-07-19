import pandas as pd

def base():
    df = pd.read_csv(r"C:\Users\elian.oliveira\Desktop\aulas\archive\salaries.csv",sep=',')
    return df

print(base()['job_title'].nunique())

for rows, col in base().iterrows():
    print(col)