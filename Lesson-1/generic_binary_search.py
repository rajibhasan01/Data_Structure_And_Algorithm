def binary_search(lo, hi, condition):
    # Set a loop for repetation
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

def locate_card(cards, query):
    def condition(mid):
        # check if the match query has another index in the list or not
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left';
            else:
                return 'found';
        elif cards[mid] < query:
            return 'left';
        else:
            return 'right';
    return binary_search(0, len(cards) - 1, condition);

# test cases added in tests array
tests = [];
# query occurs in the middle
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
});

# query is the first element
tests.append({
    'input': {
        'cards': [4, 3, 2, -1, -2],
        'query': 4
    },
    'output': 0
});

# query occurs in the last element
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, -120],
        'query': -120
    },
    'output': 7
});

# cards contains just one element
tests.append({
    'input': {
        'cards': [-2],
        'query': -2
    },
    'output': 0
});

# cards does not contain query
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, -120],
        'query': -2
    },
    'output': -1
});

# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
});

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 8, 6, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 10
});

# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
});

# large test for time complexity
tests.append({
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998
});
 

for test in tests:
    print(locate_card(**test['input']) == test['output']);