from pathlib import Path

from data_cleaning.io import load_csv, save_csv
from data_cleaning.cleaning import inspect, clean
from data_cleaning.features import add_features


def main() -> None:
    """
    Execute the complete data cleaning pipeline.
    """
    project_root = Path(__file__).resolve().parents[1]

    raw_data_path = project_root / "data" / "raw" / "sales_data_sample.csv"
    output_data_path = project_root / "data" / "processed" / "sales_data_cleaned.csv"

    # Load
    df = load_csv(raw_data_path)

    # Inspect
    inspect(df)

    # Clean
    df_cleaned = clean(df)

    # Feature engineering
    df_final = add_features(df_cleaned)

    # Save
    save_csv(df_final, output_data_path)

    print("\nData cleaning pipeline completed successfully.")


if __name__ == "__main__":
    main()
