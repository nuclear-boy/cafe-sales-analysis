import streamlit as st
import plotly.express as px

from utils import add_time_features, filter_transactions, load_data

st.set_page_config(
    page_title="Cafe Sales Dashboard",
    layout="wide",
)

LABELS = {
    "id": {
        "title": "Dashboard Penjualan Kafe",
        "subtitle": "Ringkasan data transaksi kafe yang sudah dibersihkan.",
        "language": "Bahasa",
        "filters": "Filter",
        "items": "Produk",
        "payment": "Metode pembayaran",
        "location": "Lokasi",
        "use_date": "Gunakan filter tanggal",
        "date_range": "Rentang tanggal",
        "revenue": "Total pendapatan",
        "transactions": "Jumlah transaksi",
        "average": "Rata-rata per transaksi",
        "items_sold": "Item terjual",
        "monthly": "Pendapatan per bulan",
        "top_items": "Pendapatan per produk",
        "payment_split": "Proporsi metode pembayaran",
        "location_split": "Transaksi per lokasi",
        "data": "Tabel data",
        "download": "Unduh CSV",
        "missing_dates": "transaksi tanpa tanggal dikecualikan dari grafik waktu.",
        "no_data": "Tidak ada data untuk filter yang dipilih.",
        "credit": "Sumber data: Cafe Sales - Dirty Data for Cleaning Training (Kaggle, Ahmed Mohamed).",
    },
    "en": {
        "title": "Cafe Sales Dashboard",
        "subtitle": "A summary of the cleaned cafe transaction dataset.",
        "language": "Language",
        "filters": "Filters",
        "items": "Items",
        "payment": "Payment method",
        "location": "Location",
        "use_date": "Apply date filter",
        "date_range": "Date range",
        "revenue": "Total revenue",
        "transactions": "Transactions",
        "average": "Average per transaction",
        "items_sold": "Items sold",
        "monthly": "Monthly revenue",
        "top_items": "Revenue by product",
        "payment_split": "Payment method share",
        "location_split": "Transactions by location",
        "data": "Data table",
        "download": "Download CSV",
        "missing_dates": "transactions without a date are excluded from time charts.",
        "no_data": "No data matches the selected filters.",
        "credit": "Data source: Cafe Sales - Dirty Data for Cleaning Training (Kaggle, Ahmed Mohamed).",
    },
}


@st.cache_data
def get_data():
    return add_time_features(load_data())


df = get_data()

language = st.sidebar.radio("Language / Bahasa", ["Bahasa Indonesia", "English"])
t = LABELS["id" if language == "Bahasa Indonesia" else "en"]

st.sidebar.header(t["filters"])

selected_items = st.sidebar.multiselect(
    t["items"], sorted(df["item"].unique()), default=sorted(df["item"].unique())
)
selected_payments = st.sidebar.multiselect(
    t["payment"],
    sorted(df["payment_method"].unique()),
    default=sorted(df["payment_method"].unique()),
)
selected_locations = st.sidebar.multiselect(
    t["location"],
    sorted(df["location"].unique()),
    default=sorted(df["location"].unique()),
)

use_date_filter = st.sidebar.checkbox(t["use_date"], value=False)
date_range = None
if use_date_filter:
    valid_dates = df["transaction_date"].dropna()
    date_range = st.sidebar.date_input(
        t["date_range"],
        value=(valid_dates.min().date(), valid_dates.max().date()),
        min_value=valid_dates.min().date(),
        max_value=valid_dates.max().date(),
    )

filtered = filter_transactions(
    df,
    items=selected_items,
    payment_methods=selected_payments,
    locations=selected_locations,
    date_range=date_range if use_date_filter else None,
)

st.title(t["title"])
st.caption(t["subtitle"])

if filtered.empty:
    st.warning(t["no_data"])
    st.stop()

revenue = filtered["total_spent"].sum()
transactions = filtered["transaction_id"].nunique()
average = revenue / transactions if transactions else 0
items_sold = int(filtered["quantity"].sum())

col1, col2, col3, col4 = st.columns(4)
col1.metric(t["revenue"], f"${revenue:,.2f}")
col2.metric(t["transactions"], f"{transactions:,}")
col3.metric(t["average"], f"${average:,.2f}")
col4.metric(t["items_sold"], f"{items_sold:,}")

st.divider()

dated = filtered.dropna(subset=["transaction_date"])

if dated.empty:
    st.info(t["missing_dates"])
else:
    monthly = (
        dated.groupby("month", as_index=False)["total_spent"]
        .sum()
        .sort_values("month")
    )
    monthly_chart = px.line(
        monthly,
        x="month",
        y="total_spent",
        markers=True,
        labels={"month": "", "total_spent": t["revenue"]},
        title=t["monthly"],
    )
    st.plotly_chart(monthly_chart, use_container_width=True)

left, right = st.columns(2)

item_revenue = (
    filtered.groupby("item", as_index=False)["total_spent"]
    .sum()
    .sort_values("total_spent", ascending=True)
)
item_chart = px.bar(
    item_revenue,
    x="total_spent",
    y="item",
    orientation="h",
    labels={"item": "", "total_spent": t["revenue"]},
    title=t["top_items"],
)
left.plotly_chart(item_chart, use_container_width=True)

payment_counts = filtered["payment_method"].value_counts().reset_index()
payment_counts.columns = ["payment_method", "transactions"]
payment_chart = px.pie(
    payment_counts,
    names="payment_method",
    values="transactions",
    hole=0.45,
    title=t["payment_split"],
)
right.plotly_chart(payment_chart, use_container_width=True)

location_counts = (
    filtered.groupby("location", as_index=False)["transaction_id"]
    .count()
    .rename(columns={"transaction_id": "transactions"})
)
location_chart = px.bar(
    location_counts,
    x="location",
    y="transactions",
    labels={"location": "", "transactions": t["transactions"]},
    title=t["location_split"],
)
st.plotly_chart(location_chart, use_container_width=True)

st.caption(
    f"{filtered['transaction_date'].isna().sum():,} {t['missing_dates']}"
)

with st.expander(t["data"]):
    st.dataframe(filtered, use_container_width=True)
    st.download_button(
        label=t["download"],
        data=filtered.to_csv(index=False).encode("utf-8"),
        file_name="clean_cafe_sales_filtered.csv",
        mime="text/csv",
    )

st.caption(t["credit"])
