def is_power_of_2(number):
    if type(number) is not int:
        return 'Please provide a valid integer';
    while number > 1:
        if number%2 != 0:
            return False;
        number = number // 2;
    return True;

number = int(input('Enter the integer here: '));
result = is_power_of_2(number);

if type(result) is not bool:
    print(result);
else:
    if result:
        print(f'{number} is a number that is the power of 2.');
    else:
        print(f'{number} is not the power of 2.');
