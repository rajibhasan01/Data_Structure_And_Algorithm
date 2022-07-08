def armstrong(number):
    if type(number) is not int:
        return 'please input a valid integer';
    base = base_count(number);
    return is_armstrong(number, base);

def base_count(number):
    count = 0;
    while number > 0:
        count += 1;
        number = number // 10;
    return count;
        
def is_armstrong(number, base):
    new_number = 0;
    previous_number = number;
    while number > 0:
        new_number = new_number + ((number%10) ** base);
        number = number // 10;
    
    return previous_number == new_number;

number = int(input('Enter the integer number: '));
result = armstrong(number);

if result:
    print(f'{number} is an Armstrong number.');
else:
    print(f'{number} is not an Armstrong number.');