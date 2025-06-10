import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel(
    r"C:\Users\law_m\Documents\Oysters\oyster_data_master.xlsx",
    sheet_name='Oyster Counts'
)

grouped = df.groupby(['Site', 'Round'])[
    'Total Spat (0-25 mm)'].sum().unstack(fill_value=0)

sites = grouped.index
rounds = grouped.columns
x = np.arange(len(sites))
width = 0.72 / len(rounds)

colors = ["#556B2F", "#8F9779", "#A0522D", "#2E8B57", "#6B4226"]

plt.figure(figsize=(6.5, 4))

for i, round_num in enumerate(rounds):
    plt.bar(x + i * width, grouped[round_num], width,
            label=f'{round_num}', color=colors[i % len(colors)], zorder=3)

plt.xlabel('Site', fontsize=9.25)
plt.ylabel('Number of Oysters', fontsize=9.25)
plt.title('Number of Spat-Sized Oysters per Site by Round')

plt.xticks(x + width * (len(rounds) - 1) / 2, sites,
           rotation=45, horizontalalignment='right', fontsize=7)
plt.legend(fontsize=8.25)
plt.ylim(0, 3000)
plt.grid(axis='y', zorder=0)

plt.tight_layout()
plt.show()
