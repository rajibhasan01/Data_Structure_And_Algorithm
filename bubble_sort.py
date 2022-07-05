def bubble_sort(list):
    if len(list) <= 1:
        return list;
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j];
                list[j] = list[j+1];
                list[j+1] = temp;
    return list;

print(bubble_sort([1,7,2,3,8,10,1]));