# Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

"""
    problem: We need to write a program that can find the total rotation of a number in a sorted list. In this case we need to remember the time complexity should not be greater than O(log N).
"""
"""
    Inputs: nums: A sorted rotated list e.g. [7, 9, 3, 5, 6]
    Outputs: rotations: The number of times the sorted list was rotated e.g. 2.
"""


def count_rotations(nums):
    position = 0;
    while position < len(nums):
        if position > 0 and nums[position - 1] > nums[position]:
            return position;
        position += 1;
    return 0;


tests = [];
tests.append({
    'input':{
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14],
    },
    'output': 3
});

tests.append({
    'input':{
        'nums': [5, 6, 9, 0, 2, 3, 4],
    },
    'output': 3
});

# A list of size 8 rotated 5 times.
tests.append({
    'input':{
        'nums': [5, 6, 9, 10, 21, 3, 4, 4],
    },
    'output': 5
});

# A list that was rotated just once.
tests.append({
    'input':{
        'nums': [7, 3, 5],
    },
    'output': 1
});

tests.append({
    'input':{
        'nums': [5, 6, 9, 10, 21, 22, -1, 0],
    },
    'output': 6
});
# A list that was rotated n times, where n is the size of the list
tests.append({
    'input':{
        'nums': [5, 6, 9, 10, 21, 22],
    },
    'output': 0
});

tests.append({
    'input':{
        'nums': [5],
    },
    'output': 0
});

for test in tests:
    print(count_rotations(**test['input']) == test['output']);