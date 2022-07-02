def is_valid(combination):
    stack = [];
    for par in combination:
        if par == '(':
            stack.append(1);
        else:
            if len(stack) == 0:
                return False;
            else:
                stack.pop();
    return len(stack) == 0;

def is_valid_using_variable(combination):
    diff = 0;
    for par in combination:
        if par == '(':
            diff += 1;
        else:
            if diff == 0:
                return False;
            else:
                diff -= 1;
    return diff == 0;


result = is_valid_using_variable('()()(()())(((())))');
print(result);