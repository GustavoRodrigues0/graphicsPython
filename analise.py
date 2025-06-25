import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("graficos", exist_ok=True)
df = pd.read_csv("dados.csv", parse_dates=["data"])

df["mes"] = df["data"].dt.to_period("M")
df["faturamento"] = df["quantidade"] * df["preco"]

faturamento = df.groupby("mes")["faturamento"].sum()
mais_vendidos = df.groupby("produto")["quantidade"].sum().sort_values(ascending=False)

sns.set(style="whitegrid")
plt.figure(figsize=(8, 4))
faturamento.plot(kind="bar", title="faturamento Mensal")
plt.tight_layout()
plt.savefig("graficos/faturamento_mensal.png")