def sum_all_digits(number):
    total = 0;
    while number > 0:
        total = total + number % 10;
        number = number//10;
    return total;


def product_all_digit(number):
    product = 1;
    while number > 0:
        product = product * (number % 10);
        number = number // 10;
    return product;

num = int(input("Enter the integer number here: "));
total_sum = sum_all_digits(num);
total_product = product_all_digit(num);

print(f'Sum of all Digits is: {total_sum}');
print(f'Product of all digits: {total_product}');