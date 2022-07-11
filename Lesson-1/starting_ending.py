"""
    Problem: Given an array of integers nums sorted in ascending order, find the starting and ending position of a given number.
"""

"""
    1. The numbers are sorted in increasing order.
    2. We are looking for both the start index and the end index.
"""

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo+hi)//2;
        result = condition(mid);

        if result == 'found':
            return mid;
        elif result == 'left':
            hi = mid - 1;
        else:
            lo = mid + 1;
    return -1;

def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left';
            return 'found';
        elif nums[mid] < target:
            return 'right';
        else:
            return 'left';
    return binary_search(0, len(nums) - 1, condition);

def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right';
            else:
                return 'found';
        elif nums[mid] < target:
            return 'right';
        else:
            return 'left';
    return binary_search(0, len(nums)-1, condition);

def first_and_last_position(nums, target):
    return [first_position(nums, target), last_position(nums, target)];

tests = [];
tests.append({
    'input':{
        'nums':[],
        'target': 6,
    },
    'output': [-1,-1],
});

tests.append({
    'input':{
        'nums':[1, 2, 3, 3, 3, 3, 5, 6, 8, 8, 9],
        'target': 6,
    },
    'output': [7,7],
});

tests.append({
    'input':{
        'nums':[1, 2, 3, 3, 3, 3, 5, 6, 8, 8, 9],
        'target': 3,
    },
    'output': [2,5],
});

tests.append({
    'input':{
        'nums':[1, 2, 3, 3, 3, 3, 5, 6, 8, 8, 8],
        'target': 8,
    },
    'output': [8,10],
});

tests.append({
    'input':{
        'nums':[1, 2, 3, 3, 3, 3, 5, 6, 8, 8, 9],
        'target': 11,
    },
    'output': [-1,-1],
});

for test in tests:
    print(first_and_last_position(**test['input']) == test['output']);