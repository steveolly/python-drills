def most_frequent(items: list):
    items_len = len(items)
    if not items_len:
        return None

    count = 0
    element_value = None
    for element in items:
        check = items.count(element)

        if check > count:
            count = check
            element_value = element
    return element_value
