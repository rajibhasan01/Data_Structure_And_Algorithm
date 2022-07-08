def reverse_number(number):
    number = str(number);
    new_number = '';

    for num in number:
        new_number = num + new_number;
    
    return int(new_number);

# another way
def reverse_number_2(number):
    new_number = 0;
    while number > 0:
        new_number = (new_number * 10) + (number % 10);
        number = number // 10;
    
    return new_number;



number = int(input('Enter the number: '));
print(reverse_number_2(number));