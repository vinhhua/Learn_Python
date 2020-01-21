
print("Imported my_module...")


def find_index(to_find, target) -> int:
    """Find the index of a value in a sequence"""
    for i, value in enumerate(to_find):
        if value == target:
            return i

    return -1
