def find_first_Upper(string, i):
    if len(string) != 0:
        if string[i] >= 'A' and string[i] <= 'Z':
            return string[i];
        else:
            i = i + 1;
            return find_first_Upper(string, i)
    else:
        return 0;

string = str(input('Enter the string: '));
print(find_first_Upper(string, 0));