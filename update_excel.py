import pandas as pd

file_name = "پروژه 3.xlsx"

df = pd.read_excel(file_name)

new_row = pd.DataFrame({
    " Run time for different data size": ["700KB"],
    "Alg.1": [80],
    "Alg.2": [320],
    "Alg.3": [700]
})

df = pd.concat([df, new_row], ignore_index=True)

df.to_excel(file_name, index=False)

print(df)