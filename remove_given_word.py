# remove word from string
def remove_word(string, target):
    word = '';
    string = string + ' ';
    new_string = '';
    for ch in string:
        if ch != ' ':
            word = word + ch;
        else:
            if is_matched(word, target):
                word = '';
                continue;
            else:
                new_string = new_string + word + ch;
                word = '';

    return new_string;

# checked it is matched or not
def is_matched(word, target):
    if len(word) != len(target):
        return False;

    for i in range(len(word)):
        if word[i] == target[i]:
            continue;
        else:
            return False;
    return True;


# take input from user
string = str(input('Enter the string: '));
word = str(input('Enter the word: '));

print(remove_word(string, word));