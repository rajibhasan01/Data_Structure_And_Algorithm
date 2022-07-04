str_1 = input('Enter you string here: ');
n = int(input('Enter the array length: '));
arr = list(map(int, input('Enter input: ').strip().split()))[:n];

print(str_1);
print(n);
print(arr);