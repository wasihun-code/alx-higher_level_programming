#!/usr/bin/python3
if __name__ == "__main__":
    """Mods in hidden 4"""
    import hidden_4

    mods = dir(hidden_4)
    for n in mods:
        if n[:2] != "__":
            print(n)
