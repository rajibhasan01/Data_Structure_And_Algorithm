def binary_search(list, target):
    if len(list) == 0:
        return None;
    
    left, right = 0, len(list) - 1;
    while left <= right:
        mid = (left+right)//2;
        if list[mid] == target:
            return mid;
        elif list[mid] > target:
            right = mid - 1;
        else:
            left = mid + 1;
    return None;

def verify(index, target):
    if index is not None:
        print (f'{target} is present at {index} index');
    else:
        print(f'{target} is not found in this list');

numbers = [11,10,9,8,7,6,5,4,1];

result = binary_search(numbers, 7);
verify(result, 7);

# T(n) = O(logn)
# S(n) = O(1)