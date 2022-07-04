def reverse_string(string):
    if string == "":
        return string;
    else:
        return reverse_string(string[1:]) + string[0];

string = str(input('Enter the string here: '));
print(reverse_string(string));
