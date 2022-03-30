# 1. Sum Values
def sum_values(my_dictionary):
    return sum(my_dictionary.values())


print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
print(sum_values({10: 1, 100: 2, 1000: 3}))
print('\n')

# 2. Even Keys


def sum_even_keys(my_dictionary):
    return sum([my_dictionary[key] for key in my_dictionary.keys() if key % 2 == 0])


print(sum_even_keys({1: 5, 2: 2, 3: 3}))
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))

# 3. Add Ten


def add_ten(my_dictionary):
    for key in my_dictionary.keys():
        my_dictionary[key] += 10
    return my_dictionary


print('\n')
print(add_ten({1: 5, 2: 2, 3: 3}))
print(add_ten({10: 1, 100: 2, 1000: 3}))


# 4. Values That Are Keys
def values_that_are_keys(my_dictionary):
    return [value for value in my_dictionary.values() if my_dictionary.get(value)]


print('\n')
print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))

# 5. Largest Value


def max_key(my_dictionary):
    max_value = float("-inf")
    max_key = float("-inf")
    for key in my_dictionary.keys():
        if my_dictionary[key] > max_value:
            max_key = key
    return max_key


print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
print(max_key({"a": 100, "b": 10, "c": 1000}))
print('\n')

# 1. Word Length Dict
def word_length_dictionary(words):
    words_dictionary = {}
    for word in words:
        words_dictionary[word] = len(word)
    return words_dictionary

print(word_length_dictionary(["apple", "dog", "cat"]))
print(word_length_dictionary(["a", ""]))
print('\n')

# 2. Frequency Count
def frequency_dictionary(words):
    words_dictionary = {}
    for word in words:
        if not words_dictionary.get(word):
            words_dictionary[word] = 1
        else:
             words_dictionary[word] += 1
    return words_dictionary

print(frequency_dictionary(["apple", "apple", "cat", 1]))
print(frequency_dictionary([0,0,0,0,0]))
print('\n')


# 3. Unique Values
def unique_values(my_dictionary):
    return len(list(dict.fromkeys(my_dictionary.values())))

print(unique_values({0:3, 1:1, 4:1, 5:3}))
print(unique_values({0:3, 1:3, 4:3, 5:3}))
print('\n')

# 4. Count First Letter
def count_first_letter(names):
    letters_count = {}
    for key in names.keys():
        first_letter = key[0]
        if letters_count.get(first_letter):
            letters_count[first_letter] += len(names[key])
        else:
            letters_count[first_letter] = len(names[key])
    return letters_count


print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
