def factorial(num):
    if num < 0:
        return 'Negative number';
    if num == 0:
        return 1;

    product = 1;
    for i in range(1,num+1):
        product = product * i;
    return product;

print(factorial(3));