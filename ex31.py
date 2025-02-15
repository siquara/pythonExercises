def filter_numbers(list):
    new_list = []
    for item in list:
        if isinstance(item, (int, float)):
            new_list.append(item)
    return new_list

