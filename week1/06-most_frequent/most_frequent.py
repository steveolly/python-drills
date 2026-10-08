def most_frequent(items: list):
    if not items:
        return None

    counts = {}

    for element in items:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1

    highest_count = 0
    most_frequent_element = None

    for element, count in counts.items():
        if count > highest_count:
            highest_count = count
            most_frequent_element = element

    return most_frequent_element
