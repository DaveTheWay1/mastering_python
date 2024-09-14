# copy()

sample_dict = {
    0:['a','b'],
    1:['c','d']
}

my_copy = sample_dict.copy()

print(sample_dict)
print(my_copy)

# output:
# {0: ['a', 'b'], 1: ['c', 'd']}
# {0: ['a', 'b'], 1: ['c', 'd']}

# * while they are their own version
# ! if you make a change to one, the other will change as well bc the reference points are the same!!!
# this is what is called a shadow copy
my_copy[0][0] = '!!!'
print(sample_dict)
print(my_copy)
# output:
# {0: ['!!!', 'b'], 1: ['c', 'd']}
# {0: ['!!!', 'b'], 1: ['c', 'd']}