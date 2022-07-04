def compare_string(string_1, string_2):
    if len(string_1) != len(string_2):
        return 'Not same';
    
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            return 'Not same';
        else:
            continue;
    return 'same';

str_1 = 'IncludeHelp.com';
str_2 = 'IncludeHelp.com';
print(compare_string(str_1,str_2));

