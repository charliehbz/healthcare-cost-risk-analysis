# Healthcare Cost Risk Analysis

## Project Overview
This project analyzes the key drivers of healthcare insurance costs using statistical and Bayesian modeling techniques.  
The goal is to understand how demographic and behavioral factors contribute to cost variability, uncertainty, and risk heterogeneity, and to illustrate how advanced statistical models can support data-driven decision making.

---

## Business / Analysis Questions
- What factors most strongly drive individual healthcare insurance costs?
- Do different population subgroups follow distinct cost patterns?
- How can we model highly skewed and heavy-tailed cost data more robustly?
- What insights can inform risk stratification and policy or pricing decisions?

---

## Data
- **Source:** Medical Insurance Cost Dataset (Kaggle)
- **Observations:** 1,338 insured individuals in the U.S.
- **Key variables:**
  - **Demographics:** age, sex, region
  - **Health indicators:** BMI, smoking status
  - **Family structure:** number of dependents
  - **Target variable:** annual medical insurance charges (log-transformed)

---

## Methods
The analysis follows a progressive modeling strategy:

1. **Exploratory Data Analysis (EDA)**
   - Distributional analysis of costs
   - Identification of skewness and heterogeneity
   - Examination of key relationships (age, BMI, smoking)

2. **Baseline Bayesian Linear Model**
   - Interpretable main effects
   - Full posterior uncertainty quantification

3. **Nonlinear Effects & Interactions**
   - Polynomial terms for age and BMI
   - Interaction effects for smoker vs. non-smoker populations

4. **Subgroup-Specific Modeling**
   - Separate models for smokers and non-smokers
   - Student-t likelihood to handle heavy-tailed cost distributions
   - Spline-based nonlinear modeling for complex patterns

---

## Key Findings
- **Smoking status** is the strongest driver of healthcare costs, with substantial separation between smokers and non-smokers.
- **Age and BMI** exhibit nonlinear effects, with diminishing marginal impacts at higher levels.
- **Smokers display heavy-tailed and heterogeneous cost patterns**, including evidence of bimodality.
- **Subgroup-specific Bayesian models** significantly improve predictive accuracy and uncertainty calibration compared to simple linear models.

---

## Implications for Decision Making
- Enables **risk stratification** for insurance pricing and resource allocation
- Highlights the importance of **segment-specific modeling** rather than one-size-fits-all approaches
- Demonstrates how **uncertainty-aware models** can support policy and operational decisions in healthcare analytics

---

## Repository Structure
```
.
├── data/        # Dataset or data source reference
├── notebooks/   # Step-by-step analysis notebooks
├── src/         # Reusable modeling and evaluation code
├── figures/     # Key plots and visualizations
└── report/      # Original project report (for reference)
```



---

## Notes
This project was originally developed as part of graduate coursework in Applied Mathematics & Statistics at Johns Hopkins University and has been refactored for clarity, reproducibility, and portfolio presentation.

