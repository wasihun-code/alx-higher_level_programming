#!/usr/bin/python3


class Robot:

    Three_Laws = {
        """robot doesn't harm human.""",
        """robot obeys human provided that rule one not broken.""",
        """robot protect himself except rule one and 2"""
        }

    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

