"""Suite runner for tabular robustness evaluation."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--suite", required=True)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    print(f"running suite {args.suite} with seed {args.seed}")


if __name__ == "__main__":
    main()
