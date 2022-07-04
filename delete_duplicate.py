def delete_duplicate(string):
    if len(string) == 0:
        return None;
    string = string + ' ';
    word = '';
    words = set();
    for ch in string:
        if ch != ' ':
            word = word + ch;
        else:
            words.add(word);
            word = '';
    return ' '.join(words);

string = str(input('Enter the string: '));
print(delete_duplicate(string));
