import argparse
import sys
from generator.pipeline import generate

def main():
    parser = argparse.ArgumentParser(
        description = "Generate test cases from a feature description"
    )
    parser.add_argument("feature", nargs="?", help="Feature description to test")
    parser.add_argument("--format", choices=["bdd", "table"], default="bdd")
    parser.add_argument("--llm-model", dest="llm_model", default=None)

    args = parser.parse_args()

    if not args.feature or not args.feature.strip():
        parser.print_usage()
        sys.exit(1)

    result = generate(args.feature, output_format=args.format, model=args.llm_model)
    print(result)

if __name__ == "__main__": 
    main()