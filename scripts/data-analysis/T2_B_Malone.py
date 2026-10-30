
# =====================================================
# B-2 and B-3 in one script, formatted to match screenshots
# =====================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# -----------------------
# B-2
# -----------------------

print("======== B-2 ========\n")

# (a) Build the table from a dictionary (no CSV) and display it
data = {
    "State":      ["CA",  "TX",   "FL",   "NY",   "IL",   "PA"],
    "TimeZone":   ["PST", "CST",  "EST",  "EST",  "CST",  "EST"],
    "Population": [39250, 27862,  20612,  19745,  12801,  12784],  # in thousands
    "Percentage": [12,     9,      6,      6,      4,      4]
}
df = pd.DataFrame(data)
print("Table (in thousands):")
print(df.to_string(index=False))
print()

# (b) Sort by time zone then state (ascending) and display
df_sorted = df.sort_values(["TimeZone", "State"], ascending=[True, True])
print("Sorted by TimeZone then State:")
print(df_sorted.to_string(index=False))
print()

# (c) Add RealPopulation = Population * 1000 and display
df["RealPopulation"] = df["Population"] * 1000
print("With RealPopulation column (exact numbers):")
print(df.to_string(index=False))
print()

# (d) Average, min, max (in thousands)
avg_pop = df["Population"].mean()
min_pop = df["Population"].min()
max_pop = df["Population"].max()
print(f"Average population (in thousands): {avg_pop:.2f}")
print(f"Minimum population (in thousands): {min_pop}")
print(f"Maximum population (in thousands): {max_pop}\n")

# (e) Group sum by time zone (in thousands)
group_sum = df.groupby("TimeZone", as_index=False)["Population"].sum()
print("Sum of population by TimeZone (in thousands):")
print(group_sum.to_string(index=False))
print()

# ----- Plots (formatted like the screenshots) -----

# (f) Bar chart — order the bars IL, TX, FL, NY, PA, CA (matches example image)
bar_order = ["IL", "TX", "FL", "NY", "PA", "CA"]
bar_df = df.set_index("State").loc[bar_order].reset_index()

plt.figure(figsize=(7.5, 5.2))
plt.bar(bar_df["State"], bar_df["Population"])
plt.title("Population")                     
plt.xlabel("State")                        
plt.ylabel("In Thousands")                  
plt.ylim(0, 42000)                          
plt.yticks(np.arange(0, 42001, 5000))       
plt.tight_layout()
plt.show()


plt.figure(figsize=(6.2, 6.2))
plt.pie(
    df["Population"],
    labels=df["State"],
    autopct=None,        # the image shows labels only, no percentages printed
    startangle=90
)
plt.title("Population")
plt.axis('equal')        
plt.tight_layout()
plt.show()


# -----------------------
# B-3
# -----------------------

print("======== B-3 ========\n")

# (a) Import tips.csv, histogram of Male tips
#     (Place tips.csv in the same folder as this script.)
tips = pd.read_csv("tips.csv")

male_tips = tips.loc[tips["sex"] == "Male", "tip"].astype(float)

plt.figure(figsize=(7.5, 5.0))
plt.hist(male_tips, bins=10, edgecolor="black")
plt.title("Histogram of Tips (Male Customers)")
plt.xlabel("Tip Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# (b) Mean/Std of male tips; generate 100 normal samples with those params and visualize
mean_tip = male_tips.mean()
std_tip = male_tips.std(ddof=1)

print(f"Mean tip (Male): {mean_tip:.2f}")
print(f"Standard deviation (Male): {std_tip:.2f}\n")

generated = np.random.normal(loc=mean_tip, scale=std_tip, size=100)

plt.figure(figsize=(7.5, 5.0))
plt.hist(generated, bins=10, edgecolor="black")
plt.title("Generated Normal Distribution of Tips")
plt.xlabel("Tip Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# (c) Normality test on the generated numbers (null: data are normal)
stat, p = stats.normaltest(generated)
print(f"Normality test (D’Agostino & Pearson): statistic={stat:.4f}, p-value={p:.4f}")
if p > 0.05:
    print("Fail to reject H0: data likely follow a normal distribution.")
else:
    print("Reject H0: data do not appear normal.")
