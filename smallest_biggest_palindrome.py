def is_palindrome(word):
    for i in range(len(word)):
        if word[i] == word[-i-1]:
            continue;
        else:
            return False;
    return True;

def split_string(string):
    if len(string) == 0:
        return None;
    string = string + ' ';
    word = '';
    words = [];
    for ch in string:
        if ch != ' ':
            word = word + ch;
        else:
            words.append(word);
            word = '';
    return words;

def smallest_biggest_palindrome(string):
    string = split_string(string);
    count = 0;

    for word in string:
        if is_palindrome(word):
            count += 1;
            if count == 1:
                small = big = word;
            else:
                if len(small) >= len(word):
                    small = word;
                if len(big) < len(word):
                    big = word;
        else:
            continue;

    if count == 0:
        print('No palindrome is present in the given string');
    else:
        print(small, big);

string = str(input('Enter the string here: '));
smallest_biggest_palindrome(string);

