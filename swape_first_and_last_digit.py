from math import log10


def swape_digit(num):

    base = int(log10(num));
    first_digit = num//(10**base);
    last_digit = num % 10;
    base_number = last_digit * (10**base);
    others_number = num - (first_digit*(10**base)) - last_digit;
    swape_number = base_number + others_number + first_digit;
    print(first_digit, last_digit, base_number,others_number, swape_number);


swape_digit(63108);
