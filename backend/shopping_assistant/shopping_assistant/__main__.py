import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    populate_parser = subparsers.add_parser("populate", help="populate shopping database with defaults values")

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        exit(0)
    return args

def main():
    args = parse_args()
    if args.command == "populate":
        from . import populate
