import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("پروژه 3.xlsx")

print(df)

# ------------------
# Bar Chart
# ------------------
ax = df.set_index(df.columns[0]).plot(
    kind='bar',
    figsize=(10,6)
)

plt.title("Execution Time Comparison")
plt.ylabel("Time")
plt.tight_layout()

plt.savefig("bar_chart.png", dpi=300)
plt.show()

# ------------------
# Line Chart
# ------------------
ax = df.set_index(df.columns[0]).plot(
    kind='line',
    marker='o',
    figsize=(10,6)
)

plt.title("Execution Time Trend")
plt.ylabel("Time")
plt.tight_layout()

plt.savefig("line_chart.png", dpi=300)
plt.show()

# ------------------
# Box Plot
# ------------------
plt.figure(figsize=(8,6))

df.iloc[:,1:].boxplot()

plt.title("Box Plot of Algorithms")
plt.ylabel("Execution Time")

plt.savefig("box_plot.png", dpi=300)
plt.show()

# ------------------
# Mean of Algorithm 2
# ------------------
alg2_mean = df.iloc[:,2].mean()

print("Mean of Algorithm 2 =", alg2_mean)