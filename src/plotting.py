"""Plotting utilities for exploratory analysis and model diagnostics."""

# =============================================================================
# 1. LOAD DATA & Exploratory Data Analysis
# =============================================================================
df = pd.read_csv("insurance.csv")

# Log-transform the target to stabilize variance
df["log_charges"] = np.log(df["charges"])
y = df["log_charges"].values
N = len(y)
# Set Aesthetic Style
sns.set(style="whitegrid", context="talk")

# Custom color palette
color1 = "#4C72B0"   # blue
color2 = "#DD8452"   # orange

# Plot Distribution of Charges
fig, ax = plt.subplots(1, 2, figsize=(16, 6))

# --- (A) Original charges (right-skewed) ---
sns.histplot(df["charges"], kde=True, color=color1, ax=ax[0], bins=40)
ax[0].set_title("Distribution of Charges", fontsize=20)
ax[0].set_xlabel("Charges")
ax[0].set_ylabel("Count")

# --- (B) Log-transformed charges ---
sns.histplot(df["log_charges"], kde=True, color=color2, ax=ax[1], bins=40)
ax[1].set_title("Distribution of Log(Charges)", fontsize=20)
ax[1].set_xlabel("log(Charges)")
ax[1].set_ylabel("Count")

# Remove top/right borders for clean look
sns.despine()

plt.tight_layout()
plt.show()
