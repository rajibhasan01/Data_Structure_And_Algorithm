def merge_sort(list):
    """
    Sorts a list in aschending order
    Returns a new sorted list

    # Divide: Find the midpoint of the list and divide into sublists
    # Conquer: Recursively sort the sublists created in previous step
    # Combine: Merge the sorted sublists created in previous step

    # Takes O(knlogn) time because split need O(k log n) time and merge need O(n) time
    """

    if len(list) <= 1:
        return list;

    left_half, right_half = split(list);
    left = merge_sort(left_half);
    right = merge_sort(right_half);

    return merge(left, right);

def split(list):
    # Takes overall O(k log n) time because there is a slice operation which take O(k) times
    mid = len(list)//2;
    return list[:mid], list[mid:]; # slice operation O(k) time

def merge(left, right):
    # Runs in overall O(n) time
    l = [];
    i = 0;
    j = 0;

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i]);
            i += 1;
        else:
            l.append(right[j]);
            j += 1;

    while i < len(left):
        l.append(left[i]);
        i += 1;

    while j < len(right):
        l.append(right[j]);
        j += 1;

    return l;


def verify_sorted(list):
    n = len(list);

    if n == 0 or n == 1:
        return True;

    return list[0] <= list[1] and verify_sorted(list[1:]);


arr = [54,26,93,17,77,31,44,55,20];
result = merge_sort(arr);
print(result);
print('verify sorted: ', verify_sorted(arr));
print('verify sorted: ', verify_sorted(result));


# Overall merge sort takes O(n log n) if we avoid slicing.
# S(n) = S(n)