letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
    letters = [char for char in word]
    return len(list(dict.fromkeys(letters)))
    

print(unique_english_letters("mississippi"))
print(unique_english_letters("Apple"))

def count_char_x(word, x):
    count = 0
    for char in word:
        if char == x:
            count += 1
    return count

print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))

def count_multi_char_x(word, subword):
    splits = word.split(subword)
    return(len(splits)-1)

print(count_multi_char_x("mississippi", "iss"))
print(count_multi_char_x("apple", "pp"))


def substring_between_letters(word, beging, end):
    beging_index = word.find(beging) + 1
    end_index = word.find(end)
    if(beging_index == -1 or end_index == -1):
        return word
    return word[beging_index: end_index]

print(substring_between_letters("apple", "p", "e"))
print(substring_between_letters("apple", "p", "c"))


def x_length_words(sentence, length):
    for word in sentence.split():
        if len(word) < length:
            return False
    return True

print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))



def check_for_name(sentence, name):
    return sentence.upper().find(name.upper()) != -1

print(check_for_name("My name is Jamie", "Jamie"))
print(check_for_name("My name is jamie", "Jamie"))
print(check_for_name("My name is Samantha", "Jamie"))
print('\n\n')

def every_other_letter(word):
    letters = ''
    for index in range(0, len(word), 2):
        letters = letters + word[index]
    return letters

print(every_other_letter("Codecademy"))
print(every_other_letter("Hello world!"))

