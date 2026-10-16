def has_min_length(password):
    if len(password) < 8:
        return False
    return True


def has_uppercase(password):
    return any(char.isupper() for char in password)


def has_lowercase(password):
    return any(char.islower() for char in password)


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_special(password):
    return any(not char.isalnum() and not char.isspace() for char in password)


def is_valid_password(password):
    password = password.strip()

    checkers = [has_min_length, has_uppercase,
                has_lowercase, has_digit, has_special]

    return all(checker(password)for checker in checkers)


# bonus


def get_failed_requirements(password):
    checker_dic = {
        has_min_length: "min_length",
        has_uppercase: "uppercase",
        has_lowercase: "lowercase",
        has_digit: "digit",
        has_special: "special"
    }
    failed_list = []

    for key, value in checker_dic.items():
        if not key(password):
            failed_list.append(value)
    return failed_list


print(get_failed_requirements(""))
