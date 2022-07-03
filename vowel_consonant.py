def find_vowel_consonant(string):
    i = 0;
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o','O','u','U'];
    total_vowel = [];
    totol_consonant = '';
    for ch in string:
        if ch in vowels:
            total_vowel.append(ch);
        elif ch.isalpha() and ch not in vowels:
            totol_consonant = totol_consonant + ch;
        else:
            continue;
    return total_vowel, totol_consonant;

string = 'Musfiq is a good boy!';
vowel, consonant = find_vowel_consonant(string);

print(f'vowels are -> :{vowel}');
print(f'consonant are -> : {consonant}');