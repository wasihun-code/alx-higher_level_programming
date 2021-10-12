#!/usr/bin/python3
"""Returns the string representation of a file in json."""


def save_to_json_file(my_obj, filename):
    """And this is the function meeeeeeeeeeeeeeeen

    Args:
        my_obj (str): string to be represented

    """

    import json
    with open(filename, 'w') as s:
        json.dump(my_obj, s)
