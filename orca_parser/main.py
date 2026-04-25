import argparse
from pathlib import Path
from parser.pipeline import run_pipeline

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Parse ORCA outputs into analysis tables")
    parser.add_argument(
        "root",
        type=Path,
        help="Root directory containing ORCA calculations"
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=Path("orca_parsed"),
        help="Directory where parsed CSV/JSON files will be stored",
    )
    parser.add_argument(
        "--glob",
        type=str,
        default=None,
        help="Optional filename glob/pattern filter for .out files",
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()

    results = run_pipeline(
        root_dir=args.root,
        out_dir=args.outdir,
        optional_glob=args.glob,
    )

    print("Parsing complete.")
    print(f"Jobs parsed: {len(results['jobs_table'])}")
    print(f"Complex summaries: {len(results['complex_summary_table'])}")

if __name__ == "__main__":
    main()