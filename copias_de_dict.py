"""
Template - Write a function dict_copies(my_dict, num_copies) that 
returns a list consisting of num_copies copies of my_dict
"""

# Add code here
def dict_copies(my_dict, num_copies):
   
    answer = []
    for idx in range(num_copies):
        answer.append(dict(my_dict))
    return answer

# Tests
print(dict_copies({}, 0))
print(dict_copies({}, 1))
print(dict_copies({}, 2))

test_dict = dict_copies({'a' : 1, 'b' : 2}, 2)
print(test_dict)

# Check for reference problem
test_dict[1]["a"] = 3
print(test_dict)

# Output
#[]
#[{}]
#[{}, {}]
#[{'a': 1, 'b': 2}, {'b': 2, 'a': 1}]
#[{'b': 2, 'a': 1}, {'b': 2, 'a': 3}]

# Note that you have a reference issue if the last line of output is
#[{'a': 3, 'b': 2}, {'b': 2, 'a': 3}]