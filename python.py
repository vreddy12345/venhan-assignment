1. Write a function `is_prime(n: int) -> bool` that checks if a given number is prime. 
Ans:  def is_prime(n: int) -> bool:
    
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

      # Examples of usage:
      print(is_prime(2))   # True
      print(is_prime(4))   # False
      print(is_prime(17))  # True
      print(is_prime(20))  # False


2. Write a Python function `reverse_string(s: str) -> str` that takes a string and returns its  reverse. 
def reverse_string(s: str) -> str:
    
    return s[::-1]

# Examples of usage:
print(reverse_string("hello"))    # "olleh"
print(reverse_string("Python"))   # "nohtyP"
print(reverse_string("12345"))    # "54321"
print(reverse_string(""))         # ""


3. Given a list of integers, write a function `sum_of_squares(lst: List[int]) -> int` that  returns the sum of the squares of the elements. 

from typing import List

def sum_of_squares(lst: List[int]) -> int:
    return sum(x**2 for x in lst)


4.  Write a Python program to count the frequency of each character in a given string and  return a dictionary with characters as keys and their frequencies as values. 

def count_character_frequency(input_string):
    frequency_dict = {}

    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    return frequency_dict

# Example usage:
input_string = "hello"
frequency_dict = count_character_frequency(input_string)
print(frequency_dict)

