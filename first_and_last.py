# find the first and last position an number in an array
# if not found return -1,-1

# Linear search
def first_and_last(arr, target):
    # Time complexity = O(n)
    # Space complexity = 0(1)
    for i in range(len(arr)):
        if arr[i] == target:
            start = i;
            while i+1 < len(arr) and arr[i+1] == target:
                i += 1;
            return [start, i];
    return [-1, -1];



# using Binary search (if it is sorted otherwise need to sorting first)
# find target first index
def find_first(arr, target):
    if arr[0] == target:
        return 0;

    left, right  = 0, len(arr) - 1;
    
    while left <= right:
        mid = (left+right)//2;
        if arr[mid] == target and arr[mid-1] < target:
            return mid;
        elif arr[mid] < target:
            left = mid + 1;
        else:
            right = mid - 1;
    return -1;

# Find target last index
def find_last(arr, target):
    if arr[-1] == target:
        return len(arr) - 1;

    left, right = 0, len(arr) - 1;

    while left <= right:
        mid = (left+right) //2;
        if arr[mid] == target and arr[mid + 1] > target:
            return mid;
        elif arr[mid] > target:
            right = mid - 1;
        else:
            left = mid + 1;
    return -1;


# using binary search
# Time complexity = O(logn)
#  Space complexity = 0(1)
def first_and_last_using_binary_search(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1,-1];
    start = find_first(arr, target);
    end = find_last(arr, target);
    return [start, end];



array = [1, 3, 4, 6, 6, 6, 7, 7, 8, 9];
searc_value = 2;

# Using Linear Search
result = first_and_last(array, searc_value);
print(result);

# Using Binary Search
result_2 = first_and_last_using_binary_search(array, searc_value);
print(result_2);