# Problem
"""
    We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list.
"""
# Input
"""
    1. Cards: A list of numbers sorted in decreasing order. E.g. [13, 11, 10, 7, 4, 3, 1, 0]
    2. Query: A number, whose position in the array is to be determined. E.g. 7
"""

# Output
"""
    1. Position: The position of query in the list cards. E.g. 3 in the above case (counting from 0)
"""

"""
Our function should be able to handle any set of valid inputs we pass into it. Here's a list of some possible variations we might encounter:
    1. The number query occurs somewhere in the middle of the list cards.
    2. query is the first element in cards.
    3. query is the last element in cards.
    4. the list cards contains just one element, which is query.
    5. the list cards does not contain number query.
    6. the list cards is empty.
    7. the list cards contains repeating numbers.
    8. the number query occurs at more than one position in cards.
    9. (can you think of any more variations?)
"""
from jovian.pythondsa import evaluate_test_cases;

def locate_card_linear_search(cards, query):
    # Create a variable position with the value 0
    position = 0;

    # Set up a loop for repetation
    while position < len(cards):
        # Check if element at the current position match the query
        if cards[position] == query:
            # Answer found! Return and exit ..
            return position;
        # Increment the position
        position += 1;
    # Answer not fouond! Return -1
    return -1;


def locate_card_binary_search(cards, query):
    # Check if the card list is empty or not
    if len(cards) < 1:
        return -1;
    
    # assign first index to start and last index as end
    start, end = 0, len(cards)-1;
    # Set a loop for repetation
    while start <= end:
        # calculate mid of the cards index
        mid = (start+end)//2;
        result = test_location(cards, query, mid);
        if result == 'found':
            return mid;
        elif result == 'right':
            start = mid + 1;
        else:
            end = mid - 1;
    return -1;

def test_location(cards, query, mid):
    if cards[mid] == query:
        # check if the match query has another index in the list or not
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left';
        else: 
            return 'found';
    elif cards[mid] > query:
        return 'right';
    else:
        return 'left';

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
 

evaluate_test_cases(locate_card_linear_search, tests);

# for test in tests:
#     print(locate_card_binary_search(**test['input']) == test['output']);