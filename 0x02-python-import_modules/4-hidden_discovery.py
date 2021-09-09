#!/usr/bin/python3
if __name__ == "__main__":
    """Mods in hidden 4"""
    import hidden_4 as hidden

    for name in dir(hidden):
        if name[0:2] != "__":
            print(name)
