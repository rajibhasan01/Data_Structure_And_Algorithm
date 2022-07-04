def reverse_word(string):
    word = '';
    new_string = '';
    count = 0;
    string = string + ' ';
    for ch in string:
        if ch != ' ':
            word = ch + word;
        else:
            count += 1;
            if count == 1:
                new_string = word + ch;
            else:
                new_string = new_string + ch + word;

            word = '';
    return new_string;


string = str(input('Enter the string: '));
print(reverse_word(string));
