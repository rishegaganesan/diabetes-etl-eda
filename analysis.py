import os
import argparse
from etl.schema_validation import validate_schema
from etl.cleaning import clean_data
from etl.encoding_scaling import encode_and_scale
from etl.stratified_split import stratified_split
from eda.summary_stats import summary_stats
from eda.correlations import correlation_analysis
from eda.risk_groups import risk_groups
from eda.visualizations import make_plots
from eda.multicollinearity import multicollinearity

DEFAULT_INPUT = "data/diabetes_prediction_dataset.csv"

def main():
    parser = argparse.ArgumentParser(description="Diabetes ETL + EDA Pipeline")
    parser.add_argument(
        "--input",
        type=str,
        default=DEFAULT_INPUT,
        help=f"Path to input CSV (default: {DEFAULT_INPUT})"
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--test_size", type=float, default=0.2)
    parser.add_argument("--valid_size", type=float, default=0.1)
    parser.add_argument("--out_dir", type=str, default="out")
    args = parser.parse_args()

    input_path = args.input
    if not os.path.exists(input_path):
        raise FileNotFoundError(
            f"Input dataset not found at: {input_path}\n"
            f"Place your file at: {DEFAULT_INPUT}\n"
            f"Or pass a custom path with: python main.py --input /path/to/file.csv"
        )

    out_dir = args.out_dir
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(f"{out_dir}/plots", exist_ok=True)
    os.makedirs(f"{out_dir}/splits", exist_ok=True)

    print("Starting ETL + EDA pipeline")
    print(f"Using dataset: {os.path.abspath(input_path)}")

    # ETL
    df = validate_schema(input_path)
    print("Schema validated.")

    clean_df, quarantine_df = clean_data(df)
    clean_df.to_csv(f"{out_dir}/clean.csv", index=False)
    quarantine_df.to_csv(f"{out_dir}/quarantine.csv", index=False)
    print("Cleaning completed. Clean and quarantine files saved.")

    scaled_df = encode_and_scale(clean_df)
    scaled_df.to_csv(f"{out_dir}/encode_scaled.csv", index=False)
    print("Encoding + scaling complete.")

    train, valid, test = stratified_split(clean_df, seed=args.seed, test_size=args.test_size, valid_size=args.valid_size)
    train.to_csv(f"{out_dir}/splits/train.csv", index=False)
    valid.to_csv(f"{out_dir}/splits/valid.csv", index=False)
    test.to_csv(f"{out_dir}/splits/test.csv", index=False)
    print("Stratified splits created.")

    # EDA
    summary_stats(clean_df, f"{out_dir}/summary_stats.csv")
    correlation_analysis(clean_df, f"{out_dir}/correlation.json")
    risk_groups(clean_df, f"{out_dir}/risk_groups.csv")
    make_plots(clean_df, f"{out_dir}/plots")
    multicollinearity(clean_df, f"{out_dir}/multicollinearity.txt")

    print("\nETL + EDA pipeline completed successfully!")
    print(f"All outputs saved in: {os.path.abspath(out_dir)}")

if __name__ == "__main__":
    main()
