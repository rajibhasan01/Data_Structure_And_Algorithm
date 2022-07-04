def remove_spaces(string):
    new_string = "";
    for ch in string:
        if ch >= 'a' and ch <= 'z' or ch >= 'A' and ch <= 'Z' :
            new_string = new_string + ch;
        else:
            continue;
    print(new_string);


string = str(input('Enter the string here: '));
print(string);