"""DB1 utility functions."""

from db1.api.environment_vars import DB1_PANEL_URL


def get_url(key: str) -> str:
    """Return the url of an item.

    Args:
        key (str): The key of the item.

    Returns:
        The url of the item.
    """
    return DB1_PANEL_URL + "/?key=" + key
