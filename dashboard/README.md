# Cafe Sales Dashboard

Dashboard Streamlit untuk dataset hasil cleaning pada proyek ini. Versi ini adalah **baseline**: sudah dapat dijalankan, memuat data bersih, dan menyediakan filter serta grafik utama. Pengembangan lanjutan dapat ditambahkan tanpa mengubah notebook cleaning.

## Bahasa Indonesia

### Fitur saat ini

- Toggle Bahasa Indonesia / English di sidebar.
- KPI: total pendapatan, jumlah transaksi, rata-rata per transaksi, dan item terjual.
- Grafik pendapatan bulanan (hanya transaksi dengan tanggal valid).
- Grafik pendapatan per produk, proporsi metode pembayaran, dan transaksi per lokasi.
- Filter produk, metode pembayaran, lokasi, dan rentang tanggal (opsional).
- Tabel data yang dapat difilter dan diunduh sebagai CSV.

### Cara menjalankan

Dari root repositori:

```bash
pip install -r dashboard/requirements.txt
streamlit run dashboard/app.py
```

Dashboard membaca `data/processed/clean_cafe_sales.csv`, sehingga notebook cleaning harus sudah dijalankan bila file tersebut belum ada.

### Struktur

```text
dashboard/
├── app.py              # aplikasi Streamlit
├── utils.py            # loader data, fitur waktu, dan filter
├── requirements.txt    # dependensi dashboard
└── README.md
```

### Roadmap

- Halaman terpisah untuk produk, waktu, dan pembayaran.
- Analisis hari dalam seminggu dan tren bulanan yang lebih lengkap.
- Ekspor ringkasan KPI ke CSV.
- Deploy ke Streamlit Community Cloud.
- Screenshot dashboard untuk README utama.

### Catatan data

Sebanyak 460 transaksi tidak memiliki tanggal dan dikecualikan dari grafik waktu. Nilai imputasi pada dataset hasil cleaning bersifat statistik, bukan nilai asli.

## English

### Current features

- Indonesian / English toggle in the sidebar.
- KPIs: total revenue, transaction count, average per transaction, and items sold.
- Monthly revenue chart (valid dates only).
- Revenue by product, payment method share, and transactions by location.
- Filters for items, payment methods, locations, and an optional date range.
- Filterable data table with CSV download.

### How to run

From the repository root:

```bash
pip install -r dashboard/requirements.txt
streamlit run dashboard/app.py
```

The dashboard reads `data/processed/clean_cafe_sales.csv`, so the cleaning notebook must have been executed if the file is not present.

### Structure

```text
dashboard/
├── app.py              # Streamlit application
├── utils.py            # data loader, time features, and filters
├── requirements.txt    # dashboard dependencies
└── README.md
```

### Roadmap

- Dedicated pages for products, time, and payments.
- Day-of-week analysis and richer monthly trends.
- KPI summary export to CSV.
- Deployment to Streamlit Community Cloud.
- Dashboard screenshots for the main README.

### Data notes

A total of 460 transactions have no date and are excluded from time charts. Imputed values in the cleaned dataset are statistical estimates, not ground truth.
