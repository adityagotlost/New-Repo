import argparse
import os
import sys
from typing import Optional

import pandas as pd


def compute_descriptive_statistics(df: pd.DataFrame) -> None:
    """Print basic descriptive statistics for numeric columns and counts for all columns."""
    print("Columns in dataset:", list(df.columns))

    print("\nDescriptive Statistics:\n")
    print("Maximum Values:\n", df.max(numeric_only=True))
    print("\nMinimum Values:\n", df.min(numeric_only=True))
    print("\nMean Values:\n", df.mean(numeric_only=True))
    print("\nMedian Values:\n", df.median(numeric_only=True))
    print("\nCount:\n", df.count())
    print("\nVariance:\n", df.var(numeric_only=True))
    print("\nStandard Deviation:\n", df.std(numeric_only=True))


def read_csv(path: str, sep: Optional[str], encoding: Optional[str]) -> pd.DataFrame:
    read_kwargs = {}
    if sep:
        read_kwargs["sep"] = sep
    if encoding:
        read_kwargs["encoding"] = encoding
    return pd.read_csv(path, **read_kwargs)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compute descriptive statistics for a CSV file."
    )
    parser.add_argument(
        "--file", "-f", default="data.csv", help="Path to the CSV file (default: data.csv)"
    )
    parser.add_argument(
        "--sep",
        default=None,
        help="Field separator; defaults to pandas auto-detection if omitted",
    )
    parser.add_argument(
        "--encoding",
        default=None,
        help="File encoding; if omitted pandas will attempt UTF-8",
    )

    args = parser.parse_args()
    csv_path = args.file

    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found: {csv_path}", file=sys.stderr)
        sys.exit(1)

    try:
        df = read_csv(csv_path, sep=args.sep, encoding=args.encoding)
    except Exception as exc:  # pragma: no cover - safe CLI guard
        print(f"Failed to read CSV: {exc}", file=sys.stderr)
        sys.exit(2)

    compute_descriptive_statistics(df)


if __name__ == "__main__":
    main()
