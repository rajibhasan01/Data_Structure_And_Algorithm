# Check Anagrams
# Example danger = garden
def are_anagrams(string_1, string_2):
    if len(string_1) != len(string_2):
        return False;

    freq_1 = {};
    freq_2 = {};

    for ch in string_1:
        if ch in freq_1:
            freq_1[ch] += 1;
        else:
            freq_1[ch] = 1;
    
    for ch in string_2:
        if ch in freq_2:
            freq_2[ch] += 1;
        else:
            freq_2[ch] = 1;
    
    for key in freq_1:
        if key not in freq_2 or freq_1[key] != freq_2[key]:
            return False;
    
    return True;

# another way of solving
def are_anagrams_solution2(string_1, string_2):
    if len(string_1) != len(string_2):
        return False;
    
    return sorted(string_1) == sorted(string_2);

    

result_1 = are_anagrams("garden", "danger");
print(result_1);
result_2 = are_anagrams_solution2("garden", "danger");
print(result_2);

