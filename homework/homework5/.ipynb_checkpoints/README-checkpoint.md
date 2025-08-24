Here’s a clean **README.md update** for a **Data Storage** section you can drop in your notebook repo:

---

## 📂 Data Storage

### Folder Structure

```
project/
│
├── data/
│   ├── raw/          # Original/raw data files (CSV)
│   └── processed/    # Processed or cleaned datasets (Parquet)
│
├── src/              # Utility functions and scripts
├── notebooks/        # Jupyter notebooks
└── .env              # Environment variables (paths, API keys)
```

* **`data/raw/`**: Stores unmodified source data (CSV format preferred for raw sources).
* **`data/processed/`**: Stores processed or transformed datasets in **Parquet format** for:

  * Faster I/O
  * Better compression
  * Native support for numeric/datetime types

---

### File Formats

| Folder            | Format  | Why                                                                           |
| ----------------- | ------- | ----------------------------------------------------------------------------- |
| `data/raw/`       | CSV     | Widely supported, human-readable, easy to export from APIs/scrapes            |
| `data/processed/` | Parquet | Efficient for large datasets, preserves dtypes, faster reads/writes in pandas |

---

### Reading and Writing Data

* Paths to the folders are **configurable via environment variables** in `.env`:

```text
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed
```


