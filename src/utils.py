"""Utility helpers for data loading and evaluation."""

# --- Standardize continuous predictors (store means & stds for later use) ---
scale_info = {}
for col in ["age", "bmi", "children"]:
    mean = df[col].mean()
    std = df[col].std()
    scale_info[col] = {"mean": mean, "std": std}
    df[col + "_std"] = (df[col] - mean) / std

# --- Polynomial terms ---
df["bmi_std_sq"] = df["bmi_std"] ** 2
df["age_std_sq"] = df["age_std"] ** 2

# --- Categorical predictors: one-hot encode, drop first level as baseline ---
X_cat = pd.get_dummies(df[["sex", "smoker", "region"]],
                       drop_first=True, dtype=float)

if "smoker_yes" not in X_cat.columns:
    raise ValueError("Expected column 'smoker_yes' after get_dummies.")

# --- Interaction terms ---
df["age_x_smoker"] = df["age_std"] * X_cat["smoker_yes"]
df["bmi_x_smoker"] = df["bmi_std"] * X_cat["smoker_yes"]
df["age_sq_x_smoker"] = df["age_std_sq"] * X_cat["smoker_yes"]

# --- SIMPLE SPLINE BASIS FOR AGE & BMI (for Model D) ---(We do not use this model)
# We'll use piecewise linear "truncated power" basis at 25%, 50%, 75% quantiles
age_knots = np.quantile(df["age_std"], [0.25, 0.5, 0.75])
bmi_knots = np.quantile(df["bmi_std"], [0.25, 0.5, 0.75])

for k, c in enumerate(age_knots):
    df[f"age_spline_{k}"] = np.maximum(df["age_std"] - c, 0.0)

for k, c in enumerate(bmi_knots):
    df[f"bmi_spline_{k}"] = np.maximum(df["bmi_std"] - c, 0.0)

