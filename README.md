# Cafe Sales Data Cleaning | Pembersihan Data Penjualan Kafe

**Bilingual documentation** · [Bahasa Indonesia](#bahasa-indonesia) · [English](#english)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.x%2B-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.26%2B-013243?logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)

An end-to-end data cleaning project that turns a deliberately dirty cafe sales dataset into an analysis-ready table. The project was **completed over 3 days using Python** and documents every cleaning decision, from dirty-token detection to validation.

---

## Bahasa Indonesia

### Ringkasan

Proyek ini mendokumentasikan proses pembersihan dataset penjualan kafe yang sengaja dibuat kotor untuk latihan. Dataset asli berisi nilai seperti `ERROR`, `UNKNOWN`, string kosong, tipe data yang salah, serta persentase nilai hilang yang tinggi pada beberapa kolom. Proses cleaning dilakukan secara sistematis dan dapat direproduksi, tanpa menghapus satu baris pun.

**Informasi proyek**

| Item | Detail |
|---|---|
| Penulis | Phy Fiq |
| Durasi pengerjaan | **3 hari** |
| Bahasa pemrograman | **Python 3** |
| Library utama | pandas, NumPy |
| Jumlah data | 10.000 baris x 8 kolom |
| Notebook | `notebooks/cafe_sales_cleaning_bilingual.ipynb` |
| Sumber dataset | [Cafe Sales - Dirty Data for Cleaning Training](https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training) oleh **Ahmed Mohamed** (Kaggle) |

### Struktur repositori

```text
cafe-sales-analysis/
├── data/
│   ├── raw/
│   │   └── dirty_cafe_sales.csv        # dataset asli dari Kaggle
│   └── processed/
│       └── clean_cafe_sales.csv        # hasil cleaning dari notebook
├── notebooks/
│   └── cafe_sales_cleaning_bilingual.ipynb
├── .gitignore
├── README.md
└── requirements.txt
```

### Alur cleaning

| Tahap | Masalah | Keputusan |
|---|---|---|
| Nama kolom | Spasi, kapitalisasi tidak konsisten | Diubah ke `snake_case` |
| Token kotor | `ERROR`, `UNKNOWN`, `N/A`, string kosong | Dikonversi menjadi `NaN` |
| Tipe data | Semua kolom bertipe `object` | Numerik dan tanggal dikonversi dengan `errors="coerce"` |
| `item` (969 hilang) | Tidak ada kolom acuan | Sampling proporsional dari distribusi kategori, `seed=42` |
| `payment_method` (31,78% hilang) | Terlalu banyak untuk dihapus | Sampling proporsional setelah cek rata-rata `total_spent` |
| `location` (39,61% hilang) | Terlalu banyak untuk dihapus | Sampling proporsional setelah cek rata-rata `total_spent` |
| `price_per_unit` (533 hilang) | Harga berbeda-beda per produk | Diisi dengan modus harga per produk |
| `quantity` (479 hilang) | Sebagian dapat dihitung | Dihitung dari `total_spent / price_per_unit`, sisanya sampling distribusi valid |
| `total_spent` (502 hilang/tidak konsisten) | Perhitungan tidak selalu cocok | Dihitung ulang sebagai `quantity x price_per_unit` |
| `transaction_date` (460 hilang) | Tanggal tidak bisa direkayasa | Dibiarkan kosong sebagai temuan kualitas data |

### Hasil

| Kolom | Sebelum | Sesudah | Diperbaiki |
|---|---:|---:|---:|
| `item` | 969 | 0 | 969 |
| `quantity` | 479 | 0 | 479 |
| `price_per_unit` | 533 | 0 | 533 |
| `total_spent` | 502 | 0 | 502 |
| `payment_method` | 3.178 | 0 | 3.178 |
| `location` | 3.961 | 0 | 3.961 |
| `transaction_date` | 460 | 460 | 0 (disengaja) |
| **Total** | **10.082** | **460** | **9.622** |

- 10.000 baris dipertahankan, tanpa drop data.
- `transaction_id` tetap unik untuk seluruh baris.
- `total_spent` konsisten 100% dengan `quantity x price_per_unit`.
- Imputasi bersifat statistik, bukan nilai asli, dan didokumentasikan sebagai keterbatasan.

### Cara menjalankan

```bash
git clone <your-repo-url>
cd cafe-sales-analysis

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
jupyter notebook notebooks/cafe_sales_cleaning_bilingual.ipynb
```

Jalankan notebook dari folder `notebooks/` atau dari root repositori. Path data sudah menyesuaikan keduanya.

### Insight utama

1. Persentase nilai hilang pada `payment_method` dan `location` sangat tinggi (di atas 30%), sehingga imputasi perlu diberi catatan saat data dipakai untuk keputusan bisnis.
2. Kolom `total_spent` dapat direkonstruksi sepenuhnya dari `quantity x price_per_unit`, sehingga tidak ada baris yang perlu dibuang.
3. Sebanyak 460 transaksi tanpa tanggal menjadi temuan operasional: pencatatan waktu transaksi perlu diperbaiki.
4. Distribusi kategori pada dataset ini hampir merata, sehingga sampling proporsional menjaga komposisi tetap stabil.

### Kredit dan sumber data

- Dataset: [Cafe Sales - Dirty Data for Cleaning Training](https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training) oleh **Ahmed Mohamed** di Kaggle.
- Dataset digunakan untuk latihan pembersihan data. Hak atas dataset tetap milik pembuatnya.
- Kode dan dokumentasi dibuat untuk keperluan portofolio pembelajaran.

---

## English

### Overview

This project documents the cleaning of a cafe sales dataset that was intentionally made messy for practice. The raw data contains values such as `ERROR`, `UNKNOWN`, empty strings, incorrect data types, and a high share of missing values in several columns. The cleaning process is systematic and reproducible, and not a single row was dropped.

**Project information**

| Item | Detail |
|---|---|
| Author | Phy Fiq |
| Project duration | **3 days** |
| Programming language | **Python 3** |
| Main libraries | pandas, NumPy |
| Dataset size | 10,000 rows x 8 columns |
| Notebook | `notebooks/cafe_sales_cleaning_bilingual.ipynb` |
| Dataset source | [Cafe Sales - Dirty Data for Cleaning Training](https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training) by **Ahmed Mohamed** (Kaggle) |

### Repository structure

```text
cafe-sales-analysis/
├── data/
│   ├── raw/
│   │   └── dirty_cafe_sales.csv        # original Kaggle dataset
│   └── processed/
│       └── clean_cafe_sales.csv        # output produced by the notebook
├── notebooks/
│   └── cafe_sales_cleaning_bilingual.ipynb
├── .gitignore
├── README.md
└── requirements.txt
```

### Cleaning pipeline

| Stage | Problem | Decision |
|---|---|---|
| Column names | Spaces and inconsistent casing | Standardized to `snake_case` |
| Dirty tokens | `ERROR`, `UNKNOWN`, `N/A`, empty strings | Converted to `NaN` |
| Data types | Every column was typed as `object` | Numeric and date columns converted with `errors="coerce"` |
| `item` (969 missing) | No reference column available | Proportional sampling from the category distribution, `seed=42` |
| `payment_method` (31.78% missing) | Too large to drop | Proportional sampling after checking mean `total_spent` |
| `location` (39.61% missing) | Too large to drop | Proportional sampling after checking mean `total_spent` |
| `price_per_unit` (533 missing) | Prices vary by product | Filled with the mode price per product |
| `quantity` (479 missing) | Partly derivable | Derived from `total_spent / price_per_unit`, remainder sampled from the valid distribution |
| `total_spent` (502 missing/inconsistent) | Totals did not always match | Recalculated as `quantity x price_per_unit` |
| `transaction_date` (460 missing) | Dates cannot be fabricated | Left missing and reported as a data quality finding |

### Results

| Column | Before | After | Fixed |
|---|---:|---:|---:|
| `item` | 969 | 0 | 969 |
| `quantity` | 479 | 0 | 479 |
| `price_per_unit` | 533 | 0 | 533 |
| `total_spent` | 502 | 0 | 502 |
| `payment_method` | 3,178 | 0 | 3,178 |
| `location` | 3,961 | 0 | 3,961 |
| `transaction_date` | 460 | 460 | 0 (intentional) |
| **Total** | **10,082** | **460** | **9,622** |

- All 10,000 rows were preserved; no data was dropped.
- `transaction_id` remains unique across every row.
- `total_spent` is 100% consistent with `quantity x price_per_unit`.
- Imputed values are statistical estimates, not ground truth, and are documented as a limitation.

### How to run

```bash
git clone <your-repo-url>
cd cafe-sales-analysis

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
jupyter notebook notebooks/cafe_sales_cleaning_bilingual.ipynb
```

Run the notebook from either the `notebooks/` folder or the repository root. The data paths support both locations.

### Key insights

1. Missing values in `payment_method` and `location` are very high (above 30%), so imputation should be disclosed when the data informs business decisions.
2. `total_spent` can be fully reconstructed from `quantity x price_per_unit`, so no rows need to be discarded.
3. A total of 460 transactions have no date, which is an operational finding: transaction timestamping needs improvement.
4. Category distributions in this dataset are nearly uniform, so proportional sampling keeps the composition stable.

### Credits and data source

- Dataset: [Cafe Sales - Dirty Data for Cleaning Training](https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training) by **Ahmed Mohamed** on Kaggle.
- The dataset is used for data cleaning practice. Ownership remains with its author.
- Code and documentation were produced for learning portfolio purposes.
