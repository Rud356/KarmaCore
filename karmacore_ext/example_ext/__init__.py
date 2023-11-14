from typing import Any

# Extensions metadata goes to init file
# This is just minimal example of extension

__extension_name__ = "extension1"
__version__ = "1.0.0"


def register(configuration: dict[str, Any]) -> str:
    """
    Prepares extension for work.

    :param configuration: extension specific configuration.
    :return:
    """
    pass