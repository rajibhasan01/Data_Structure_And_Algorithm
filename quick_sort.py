def quick_sort(list):
    if len(list) <= 1:
        return list;

    pivot = list.pop();
    greater_list = [];
    lower_list = [];

    for i in list:
        if i > pivot:
            greater_list.append(i);
        else:
            lower_list.append(i);

    return quick_sort(lower_list) + [pivot] + quick_sort(greater_list);

print(quick_sort([1,7,2,3,8,10,1]));