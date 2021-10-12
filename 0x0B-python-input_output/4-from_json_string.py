#!/usr/bin/python3
"""Returns the string representation of a file in json."""


def from_json_string(my_obj):
    """And this is the function meeeeeeeeeeeeeeeen

    Args:
        my_obj (str): string to be represented

    """

    import json
    with open('my_obj', 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

    return f
