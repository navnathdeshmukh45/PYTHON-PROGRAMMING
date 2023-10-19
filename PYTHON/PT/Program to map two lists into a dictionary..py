def map_lists_to_dictionary(keys, values):
    if len(keys) != len(values):
        raise ValueError("Lists must have the same length")

    dictionary = dict(zip(keys, values))
    return dictionary


# Example usage
keys_list = ['name', 'age', 'city']
values_list = ['nav', 25, 'New York']

result_dict = map_lists_to_dictionary(keys_list, values_list)
print(result_dict)
