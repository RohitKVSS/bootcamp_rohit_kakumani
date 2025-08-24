

---

## 🧹 Data Cleaning Strategy

Our cleaning logic is modularized in **`src/cleaning.py`**, making it reusable and testable.
The following functions are provided:

* **`fill_missing_median(df, columns)`**
  Fills missing values in specified numeric columns with the **median** of each column.
  *Rationale:* Median is robust against outliers and ensures no artificial skew.

* **`drop_missing(df, threshold=0.5)`**
  Drops columns or rows exceeding a given missing-value threshold.
  *Rationale:* Prevents noisy or incomplete features from impacting downstream models.

* **`normalize_data(df, columns)`**
  Applies min–max scaling to bring selected numeric columns into the range \[0,1].
  *Rationale:* Normalization ensures comparability across features and improves model stability.

### Workflow in Jupyter

1. **Load raw dataset** from `data/raw/`.
2. **Apply cleaning functions** from `src/cleaning.py`.
3. **Save cleaned dataset** to `data/processed/`.
4. **Compare original vs cleaned dataset** (missing counts, distribution, shape).
5. **Document assumptions** (e.g., threshold choice, median vs mean) directly in the notebook.

### Assumptions & Risks

* Assumes numeric columns are correctly typed (`float`, `int`) before applying cleaning.
* Median imputation may not capture time-series structure (risk of leakage in financial data).
* Dropping high-NA columns could remove informative features — threshold choice is critical.
* Normalization is not suitable for sparse or categorical features without preprocessing.

---


