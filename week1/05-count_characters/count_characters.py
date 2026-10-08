import time

start = time.time()


def count_characters(text) -> dict:
    count_letters = 0
    count_numbers = 0
    count_spaces = 0
    count_special = 0

    for char in text:
        if char.isalpha():
            count_letters += 1
        elif char.isdigit():
            count_numbers += 1
        elif char == " ":
            count_spaces += 1
        else:
            count_special += 1
    return dict(letters=count_letters, numbers=count_numbers, spaces=count_spaces, special=count_special)


# def count_characters(text) -> dict:
#     result = {
#         "letters": 0,
#         "numbers": 0,
#         "spaces": 0,
#         "special": 0
#     }

#     for char in text:
#         if char.isalpha():
#             result["letters"] += 1
#         elif char.isdigit():
#             result["numbers"] += 1
#         elif char == " ":
#             result["spaces"] += 1
#         else:
#             result["special"] += 1
#     return result


end = time.time()

print("Execution time:", end - start, "seconds")
