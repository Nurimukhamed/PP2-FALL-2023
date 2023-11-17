def all_elements_true(input_tuple):
    return all(input_tuple)

sample_tuple = (True, True, True, True)
result = all_elements_true(sample_tuple)

print("All elements in the tuple are True." if result else "Not all elements in the tuple are True.")
