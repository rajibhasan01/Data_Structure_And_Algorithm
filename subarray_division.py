"""
    Problem:
    --------
    We need to write a code that find the number of times that sum of contiguous sub array
    of an array/list is equal to the given date and the lenght of the sub array is equal the given month.
"""

"""
    Input:
    ------
    Input will be a list of integer where total element of the list is greater or equal than 1 and less or equal than 100.
    Given date will be greater or equal 1 and less or equal than 31.
    Given month will be greater or equal 1 and less or equal than 12.
"""

"""
    Example:
    Input:  5
            1 2 1 3 2
            3 2

    output: 2
"""

def count_ways(lists, date, month):
    if len(lists) < 1 and len(lists) > 100:
        return 0;
    if date < 1 and date > 31:
        return 0;
    if month < 1 and month > 12:
        return 0;

    count = 0;

    for position in range(len(lists)):
        if month <= len(lists) - position:
            sum = 0;
            for j in range(position, position+month):
                sum += lists[j];
            if sum == date:
                count += 1;
    return count;

tests = [];
tests.append({
    'input':{
        'lists': [1, 2, 1, 3, 2],
        'date': 3,
        'month': 2
    },
    'output': 2
});

tests.append({
    'input':{
        'lists': [1, 1, 1, 1, 1, 1],
        'date': 3,
        'month': 2
    },
    'output': 0
});

tests.append({
    'input':{
        'lists': [4],
        'date': 4,
        'month': 1
    },
    'output': 1
});

for test in tests:
    count = 0;
    if count_ways(**test['input']) != test['output']:
        count += 1;
if count == 0:
    print('All the test case passed. Now Input manually for other test case');


n = int(input('Enter the length of the list here: '));
lists = list(map(int, input('Enter the list element here: ').strip().split()))[:n];
date_month = list(map(int, input("Enter the date and month here: ").strip().split()));
print(date_month);

print(count_ways(lists, date_month[0], date_month[1]));
