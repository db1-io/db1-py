"""DB1 CLI script for resource item."""

from db1.api._item import await_next_item, delete_item, get_item, listen, set_item


# Handle operation delete
def handle_operation_delete(args):
    key = args["key"]
    delete_item(key)
    print("Item with key " + key + " deleted.")


# Handle operation get_value
def handle_operation_get_value(args):
    key = args["key"]
    print(get_item(key))


# Handle operation set_value
def handle_operation_set_value(args):
    key = args["key"]
    if not args["value"]:
        print("Positional argument `value` is required on `set`.\n")
        print_missing_value()
        return

    value = args["value"]
    set_item(key, value)
    print("Value " + value + " set on item with key " + key + ".")


# Handle operation listen
def handle_operation_listen(args):
    key = args["key"]

    def print_set_value(value):
        print("Value set to " + value)

    def print_delete():
        print("Item deleted")

    def print_open():
        print("Connection opened")

    def print_error(error):
        print("Error: " + error)

    def print_close(close_status_code, close_msg):
        print("Connection closed: " + close_msg + " " + close_status_code)

    listen(
        key,
        on_set_value=print_set_value,
        on_delete=print_delete,
        on_open=print_open,
        on_error=print_error,
        on_close=print_close,
    )


# Handle operation await_next_value
def handle_operation_await_next_value(args):
    key = args["key"]
    print(await_next_item(key))


OPERATIONS = [
    ["delete", "db1 delete", handle_operation_delete],
    ["get", "db1 get", handle_operation_get_value],
    ["set", "db1 set", handle_operation_set_value],
    ["listen", "db1 listen", handle_operation_listen],
    [
        "await",
        "db1 await",
        handle_operation_await_next_value,
    ],
]


def handle_resource_item(args):
    # print("Resource is item.")

    if not args["operation"]:
        print("Positional argument `operation` is required.\n")
        print_available_operations()
        return

    if not args["key"]:
        print("Positional argument `key` is required.\n")
        print_missing_id()
        return

    operation = args["operation"]

    for operation_handler in OPERATIONS:
        if operation_handler[0] == operation:
            operation_handler[2](args)
            return

    print(f"Operation `{operation}` does not exist.\n")
    print_available_operations()


def print_available_operations():
    print("Operations:")
    for operation_handler in OPERATIONS:
        print(f"  {operation_handler[1]}")
    print("\nOr try: db1 -h\n")


def print_missing_id():
    print("Example: \n db1 get some_item_key\n")
    return


def print_missing_value():
    print("Example: \n db1 set some_item_key 123\n")
    return
