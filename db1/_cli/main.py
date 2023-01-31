"""Main script for the DB1 CLI."""

import argparse

from db1._cli.item import handle_resource_item


def main():
    """Main entry point for the DB1 CLI."""

    parser = argparse.ArgumentParser(description="DB1 Command Line Interface (CLI).")

    # Positional arguments
    parser.add_argument(
        "operation",
        type=str,
        nargs="?",
        help="Name of operation (e.g. set, get).",
    )
    parser.add_argument(
        "key",
        type=str,
        nargs="?",
        help="Key of the item (e.g. some_item_key).",
    )
    parser.add_argument(
        "value",
        type=str,
        nargs="?",
        help="Some operations require a value (e.g. 123, hello).",
    )

    # Argument flags (optional)
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Print the version number and exit.",
    )

    args = vars(parser.parse_args())

    if args["version"]:
        print("0.1.2")
        return

    handle_resource_item(args)
    return


if __name__ == "__main__":
    main()
