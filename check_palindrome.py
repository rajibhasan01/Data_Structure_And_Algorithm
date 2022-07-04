def is_palindrome(string):
    for i in range(len(string)):
        if string[i] == string[-i-1]:
            continue;
        else:
            return False;
    return True;


print(is_palindrome('abcdcbaa'));