from tools import *
from tools.col import myzip

# Test the rule
check_simp_called()

# Test the functions
result_add = add(3, 5)
result_subtract = subtract(10, 3)
result_sum_of_digits = sum_of_digits(234)
result_is_palindrome = is_palindrome(1221)

# Test the myzip function
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result_zip = myzip(list1, list2)

# Print results
print(f"Add: {result_add}")
print(f"Subtract: {result_subtract}")
print(f"Sum of Digits: {result_sum_of_digits}")
print(f"Is Palindrome: {result_is_palindrome}")
print(f"myzip: {list(result_zip)}")
