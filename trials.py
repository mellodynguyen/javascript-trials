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
print(censor_vowels("dog"))


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
