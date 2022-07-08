# Count Occurrence of a Digit in a Number

def count_number(number, target):
    if type(number) is not int and type(target) is not int:
        return 'Please provide a valid integer';
    count = 0;
    while number > 0:
        digit = number % 10;
        if digit == target:
            count += 1;
        number = number // 10;
    
    return count;

number = int(input('Enter the number here: '));
target = int(input('Enter the target here: '));
result = count_number(number, target);
print(f'{target} is found {result} times in the number');