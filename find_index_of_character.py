def find_index(string, target):
    index = [];
    for i in range (len(string)):
        if string[i] == target:
            index.append(i);
        else:
            continue;
    return index;

input_string = 'Hi there, how are you?';
print(find_index(input_string, 'o'));