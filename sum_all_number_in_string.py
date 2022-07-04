def sum_number_in_string(string):
    if len(string) == 0:
        return 0;

    sum = 0;
    for i in string:
        if i.isdigit():
            sum += int(i);
        else:
            continue
    return sum;

string = input('Enter the string here: ');
print(sum_number_in_string(string));