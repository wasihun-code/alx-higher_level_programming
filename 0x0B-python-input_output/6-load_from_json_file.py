#!/usr/bin/python3
"""Documentation for object creating"""


def load_from_json_file(filename):
    """Creates an onject from json file."""

    import json

    with open(filename) as f:
        parsed_json = json.load(f)

    return parsed_json
