def reverse_string(string):
    new_string = '';
    for ch in string:
        new_string = ch + new_string;

    return new_string;

string = str(input('Enter string here: '));
print(f'Your reverse string is: {reverse_string(string)}');