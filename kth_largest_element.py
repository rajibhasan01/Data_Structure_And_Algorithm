def kth_largest_element(arr, k):
    if len(arr) < k:
        return 'Does not exist';
    
    # arr = sorted(arr); # t(n) = O(nlogn)
    # return arr[-k];

    for i in range(k-1):
        arr.remove(max(arr));
    
    return max(arr);

arr = [4,2,9,7,5,6,7,1,3];
k = 4

print(kth_largest_element(arr, k));