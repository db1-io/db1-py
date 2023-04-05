"""Main script for the DB1 CLI."""

import argparse

from db1._cli.item import handle_resource_item


def main():
    """Main entry point for the DB1 CLI."""

    description = (
        "DB1 Command Line Interface (CLI).\n\n"
        "On set values are attempted to be decoded as JSON, otherwise as strings.\n"
        "On get values are attempted to be encoded as JSON, otherwise using the print function.\n"
    )
    parser = argparse.ArgumentParser(
        description=description, formatter_class=argparse.RawTextHelpFormatter
    )

    # Positional arguments
    parser.add_argument(
        "operation",
        type=str,
        nargs="?",
        help="Name of operation (e.g. set, get, delete).",
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
    parser.add_argument(
        "-pp",
        "--pretty-print",
        action="store_true",
        help="Pretty print the value on get.",
    )

    args = vars(parser.parse_args())

    if args["version"]:
        print("0.1.6")
        return

    handle_resource_item(args)
    return


if __name__ == "__main__":
    main()
