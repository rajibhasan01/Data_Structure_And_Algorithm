def lower_uper_case(string):
    if len(string) == 0:
        return 0;

    upper = 0;
    lower = 0;

    for ch in string:
        if ch.isalpha():
            if ch >= 'A' and ch <= 'Z':
                upper += 1;
            else:
                lower += 1;
        else:
            continue;
    return upper, lower;

string = 'Musfiq is a gooD boy!';
print(lower_uper_case(string));