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

# =============================================================================
# DESIGN MATRICES FOR DIFFERENT MODELS
# =============================================================================

# ===== Model A: Baseline (main effects only, no polys or interactions) =====
X_cont_A = df[["age_std", "bmi_std", "children_std"]]
X_full_A = pd.concat([X_cont_A, X_cat], axis=1)
X_A = np.column_stack([np.ones(N), X_full_A.to_numpy()])
param_names_A = ["alpha"] + list(X_full_A.columns)

# ===== Model B: BMI^2 + smoker interactions ===== (We do not use this model)
X_cont_B = df[["age_std", "bmi_std", "bmi_std_sq", "children_std"]]
X_full_B = pd.concat(
    [X_cont_B, X_cat, df[["age_x_smoker", "bmi_x_smoker"]]],
    axis=1
)
X_B = np.column_stack([np.ones(N), X_full_B.to_numpy()])
param_names_B = ["alpha"] + list(X_full_B.columns)

# ===== Model C: BMI^2 + AGE^2 + smoker interactions =====
X_cont_C = df[["age_std", "age_std_sq", "bmi_std", "bmi_std_sq", "children_std"]]
X_full_C = pd.concat(
    [X_cont_C, X_cat, df[["age_x_smoker", "bmi_x_smoker", "age_sq_x_smoker"]]],
    axis=1
)
X_C = np.column_stack([np.ones(N), X_full_C.to_numpy()])
param_names_C = ["alpha"] + list(X_full_C.columns)

# ===== Model D: Student-t + splines for age and BMI (nonlinear mean) =====
X_cont_D = df[
    ["age_std", "age_std_sq", "bmi_std", "bmi_std_sq", "children_std",
     "age_spline_0", "age_spline_1", "age_spline_2",
     "bmi_spline_0", "bmi_spline_1", "bmi_spline_2"]
]
X_full_D = pd.concat(
    [X_cont_D, X_cat, df[["age_x_smoker", "bmi_x_smoker", "age_sq_x_smoker"]]],
    axis=1
)
X_D = np.column_stack([np.ones(N), X_full_D.to_numpy()])
param_names_D = ["alpha"] + list(X_full_D.columns)

print("Number of observations:", N)
print("\nModel A (baseline) predictors:")
for name in param_names_A:
    print("  -", name)
print("\nModel B (extended) predictors:")
for name in param_names_B:
    print("  -", name)
print("\nModel C (extended + age^2) predictors:")
for name in param_names_C:
    print("  -", name)
print("\nModel D (Student-t + splines) predictors:")
for name in param_names_D:
    print("  -", name)
