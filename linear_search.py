def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """
    for index in range(len(list)):
        if list[index] == target:
            return index;
    return None;

def verify(index, target):
    if index is not None:
        print(f"{target} found at {index} index");
    else:
        print(f"{target} not found in list");

numbers = [1,2,3,4,5,6,9,10];

result = linear_search(numbers, 6);
verify(result, 6);