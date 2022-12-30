"""DB1 CLI script for resource item."""

from db1.api.item import await_next_value, create, delete, get_value, listen, set_value


# Handle operation create
def handle_operation_create(args):
    resource_id = args["id"]
    create(resource_id)
    print("Item with resource_id " + resource_id + " created.")


# Handle operation delete
def handle_operation_delete(args):
    resource_id = args["id"]
    delete(resource_id)
    print("Item with resource_id " + resource_id + " deleted.")


# Handle operation get_value
def handle_operation_get_value(args):
    resource_id = args["id"]
    print(get_value(resource_id))


# Handle operation set_value
def handle_operation_set_value(args):
    resource_id = args["id"]
    if not args["value"]:
        print("Positional argument `value` is required on `set_value`.\n")
        print_missing_value()
        return

    value = args["value"]
    set_value(resource_id, value)
    print("Value " + value + " set on item with ID " + resource_id + ".")


# Handle operation listen
def handle_operation_listen(args):
    resource_id = args["id"]

    def print_set_value(value):
        print("Value set to " + value)

    def print_create():
        print("Item created")

    def print_delete():
        print("Item deleted")

    def print_open():
        print("Connection opened")

    def print_error(error):
        print("Error: " + error)

    def print_close(close_status_code, close_msg):
        print("Connection closed: " + close_msg + " " + close_status_code)

    listen(
        resource_id,
        on_set_value=print_set_value,
        on_create=print_create,
        on_delete=print_delete,
        on_open=print_open,
        on_error=print_error,
        on_close=print_close,
    )


# Handle operation await_next_value
def handle_operation_await_next_value(args):
    resource_id = args["id"]
    print(await_next_value(resource_id))


OPERATIONS = [
    ["create", "db1 create", handle_operation_create],
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

    if not args["id"]:
        print("Positional argument `id` is required.\n")
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
    print("Example: \n db1 get some_path\n")
    return


def print_missing_value():
    print("Example: \n db1 set some_path 123\n")
    return
