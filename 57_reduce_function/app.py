# the reduce() function applies a function to an iterable and reduces it to a single cumulative value.

import functools

letters = ["H", "E", "L", "L", "O"]

word = functools.reduce(lambda x, y: x + y, letters)

print(word)