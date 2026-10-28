from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "processed" / "clean_cafe_sales.csv"


def load_data(path: Path | str = DATA_PATH) -> pd.DataFrame:
    """Load the cleaned cafe sales dataset."""
    return pd.read_csv(path, parse_dates=["transaction_date"])


def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add date-based helper columns used by the dashboard."""
    enriched = df.copy()
    enriched["year"] = enriched["transaction_date"].dt.year
    enriched["month"] = enriched["transaction_date"].dt.to_period("M").astype(str)
    enriched["month_name"] = enriched["transaction_date"].dt.strftime("%b")
    enriched["day_of_week"] = enriched["transaction_date"].dt.day_name()
    return enriched


def filter_transactions(
    df: pd.DataFrame,
    items: list[str] | None = None,
    payment_methods: list[str] | None = None,
    locations: list[str] | None = None,
    date_range: tuple | None = None,
) -> pd.DataFrame:
    """Filter the dataset by category selections and an optional date range."""
    filtered = df

    if items:
        filtered = filtered[filtered["item"].isin(items)]
    if payment_methods:
        filtered = filtered[filtered["payment_method"].isin(payment_methods)]
    if locations:
        filtered = filtered[filtered["location"].isin(locations)]

    if date_range and len(date_range) == 2:
        start = pd.to_datetime(date_range[0])
        end = pd.to_datetime(date_range[1])
        filtered = filtered[
            filtered["transaction_date"].notna()
            & filtered["transaction_date"].between(start, end)
        ]

    return filtered
