def reverse_array(list):
    n = len(list)-1;
    arr = [];

    while n >= 0:
        arr.append(list[n]);
        n -= 1;
    return arr;

length = int(input('Enter the number of element in the Array: '));
list = [];

for i in range(length):
    element = input();
    list.append(element);

result = reverse_array(list);
print('Reverse Array is: ', result);