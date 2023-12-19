"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)
    return None


def get_all_evens(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums

def get_odd_indices(items):
    odd_nums = []
    nums = items
    for num in nums:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums

def print_as_numbered_list(items):
    for i, item in enumerate(items):
            print(f"{i}, {item}")
    return None


def get_range(start, stop):
    nums = []
    # i = 0
    # while i < 10:
    #     i + 1 
    #     print (i)

    for num in range(start, stop):
        nums.append(num)
    # return nums
    print(nums)
# input 0 - 10 (start, stop)
# expected output
# 0, 1, 2, 3, 4, 5, 6, 7, ... 
# 10 - 20
# 10, 11, 12 ... 

def censor_vowels(word):
    censored_word = []
    vowel = 'aeiou'
    
    for letter in word:
        if letter in vowel:
            censored_word.append('*')
        else:
            censored_word.append(letter)
    
    return ''.join(censored_word)
    # return word



def snake_to_camel(string):
    camelcase = []

    for word in string.split('_'):
        camelcase.append(f'{word[0].upper()}{word[1:]}')
    
    # expected ouput is HelloWord
    return ''.join(camelcase)


def longest_word_length(words):
    longest = len(words)

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest

def truncate(string):
    result = []
    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)
    
    return ''.join(result)


def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1

        if parens > 0:
            return False
    return parens < 0


def compress(string):
    compressed = []

    curr_char = ''
    char_count = 0
    for char in string:
        if char != curr_char:
            compressed.append(curr_char)

            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char
            char_count = 0

        char_count += 1

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return ''.join(compressed)
