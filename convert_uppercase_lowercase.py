def convert_upperCase(string):
    strng_1 = '';
    for ch in string:
        if ch.isalpha():
            if ord(ch) >= 97:
                ch = chr(ord(ch) -32);
                strng_1 = strng_1 + ch;
            else:
                strng_1 = strng_1 + ch;

    return strng_1;

string = 'Musfiq is a gooD boy!';
print(convert_upperCase(string));