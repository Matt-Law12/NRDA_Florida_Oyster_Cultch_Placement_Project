import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel(
    r"C:\Users\law_m\Documents\Oysters\oyster_data_master.xlsx",
    sheet_name='Oyster Sizes'
)

grouped = df.groupby('Round')['Size'].agg(
    ['mean', 'std', 'count']).reset_index()

grouped['se'] = grouped['std'] / np.sqrt(grouped['count'])
grouped.columns = ['Round', 'Average Size', 'Std Dev', 'Count', 'SE']

colors = ['#D8B3D0', '#9B59B6', '#8A2BE2', '#4B0082', "#2E1A66"]

plt.figure(figsize=(6.5, 4))
bars = plt.bar(grouped['Round'],
               grouped['Average Size'],
               yerr=grouped['SE'],
               capsize=5,
               width=0.45,
               color=colors[:len(grouped)],
               zorder=3)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 1.25,
             f'{height:.2f}', ha='center', va='bottom')

plt.title('Average Shell Height in Apalachicola Bay')
plt.ylabel('Shell Height (mm)')
plt.xticks(rotation=0)
plt.ylim((0, 45))
plt.grid(axis='y', zorder=0)

plt.tight_layout()
plt.show()
