dictionary = {
    'test_1':'pass',
    'test_2':'fail',
    'test_3': 'in progress'
}

print(dictionary.__contains__('test_1'))
# True

dictionary.__delitem__('test_3')
print(dictionary)
# {'test_1': 'pass', 'test_2': 'fail'}

print(dictionary.__sizeof__())
# returns size of dictionary in memory, in bytes
# output: 216

print(dictionary.keys())
# output: dict_keys(['test_1', 'test_2'])