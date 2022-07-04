def toggle_string(string):
    new_string = '';
    for ch in string:
        if ch.isalpha():
            if ord(ch) >= 92:
                new_string = new_string + chr(ord(ch)-32);
            else:
                new_string = new_string + chr(ord(ch)+32);
        else:
            new_string = new_string + ch;
    return new_string;

string = 'Musfiq is a gooD boy!';
print(toggle_string(string));