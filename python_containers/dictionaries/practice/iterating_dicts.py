dictionary = {
    'test_1':'success',
    'test_2':'in progress',
    'test_3':'fail',
    'study':True
}

for key, val  in dictionary.items():
    print(f"{key} - {val}")
# output:
# test_1 - success
# test_2 - in progress
# test_3 - fail
# study - True

print(dictionary.get("study"))
# output:
# True

if 'study' in dictionary:
    print(dictionary['study'])
# output:
# True