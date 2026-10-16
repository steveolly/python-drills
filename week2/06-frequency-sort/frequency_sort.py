def frequency_sort(items):
    if not items:
        return []
    num_dic = {}

    for item in items:
        num_dic[item] = num_dic.get(item, 0) + 1
    num_dic = dict(sorted(num_dic.items(), key=lambda x: (-x[1], x[0])))

    result = []
    for num, freq in num_dic.items():
        result += [num] * freq
    return result
