import pandas as pd

df = pd.read_excel("پروژه 3.xlsx")

new_row = pd.DataFrame({
    "Data size": ["700KB"],
    "Alg.1": [80],
    "Alg.2": [320],
    "Alg.3": [700]
})

df = pd.concat([df, new_row], ignore_index=True)

df.to_excel("updated_data.xlsx", index=False)

print(df)