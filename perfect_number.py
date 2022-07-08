def is_perfect_number(number):
    if type(number) is not int:
        return 'Plese enter a valid integer';
    sum = 0;
    i = 1;
    mid = number // 2;
    while i <= mid:
        if number % i == 0:
            sum += i;
        i += 1;
    return sum == number;

number = int(input('Enter the integer here: '));
result = is_perfect_number(number);

if type(result) is bool and result:
    print(f'{number} is a perfect number.');
elif type(result) is bool:
    print(f'{number} is not a perfect number.');
else:
    print(result);