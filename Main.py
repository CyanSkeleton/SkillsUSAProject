import re  # This is for removing all whitespaces and non-alphanumeric characters


# If a comment is split across two lines or a comment is referring to a line above or below it, it's
# probably due to PEP8's 120 characters per line limit

def is_palindrome(string, case_insensitive=False, whitespace_insensitive=False, ignore_punctuation=False):
    if not isinstance(string, str):  # Check if the input is a String or not. If not it returns an error
        if not isinstance(string, int) or isinstance(string, bool):
            # The above line checks if the input is not an int or is a bool (a subclass of int)
            # to make sure correct grammar is used in the error message
            raise TypeError(f"The input must be a String, not a {type(string).__name__}")  # Raise type error
        else:
            raise TypeError(f"The input must be a String, not an {type(string).__name__}")
            # The above line raises type error, but it's an "an" instead of an "a"

    if not isinstance(case_insensitive, bool):  # Check if case_insensitive is a boolean
        raise TypeError(f"case_insensitive must be a Boolean, not a {type(case_insensitive).__name__}")
        # The above line raises a type error
    if not isinstance(whitespace_insensitive, bool):  # Check if whitespace_insensitive is a boolean
        raise TypeError(f"whitespace_insensitive must be a Boolean, not a {type(whitespace_insensitive).__name__}")
        # The above line raises a type error
    if not isinstance(ignore_punctuation, bool):  # Check if ignore_punctuation is a boolean
        raise TypeError(f"ignore_punctuation must be a Boolean, not a {type(ignore_punctuation).__name__}")
        # The above line raises a type error

    if case_insensitive:  # Check if case_insensitive is true or not
        string = string.lower()  # Converts the input into all lowercase if it is

    if whitespace_insensitive:  # Check if case_insensitive is true or not
        string = re.sub(pattern=r"\s", repl="", string=string)  # Uses regex to remove all whitespace characters, \s is
        # a shorthand for [\t\n\r\f\v] with [] meaning any character in the brackets, \t = tabs, \n = newlines,
        # \r = carriage returns, \f = form feeds, and \v = vertical tabs. re.sub substitutes any characters given in the
        # first argument with the string in the second argument

    if ignore_punctuation:  # Check if case_insensitive is true or not
        string = re.sub(pattern=r"[^a-zA-Z0-9\s]", repl="", string=string)
        # The line above uses regex to remove all non-alphanumeric characters. [] means any of the characters in the
        # brackets, ^ inverts it so it means everything not covered by the brackets given, a-z covers lowercase,
        # A-Z covers uppercase, 0-9 covers numbers and \s covers whitespace. re.sub does the same thing as explained in
        # the multi-line comment above

    input_list = list(string)  # Convert String into List
    reversed_list = list(string)  # Make a copy of the list under a different variable name
    reversed_list.reverse()  # Reverse the order of the copy
    # This was done because .reverse() doesn't return anything. so I couldn't
    # directly assign it like "reversed_list = input_list.reverse()"

    if input_list == reversed_list:  # Checks if the two lists are equal
        return True  # Returns True if they are
    else:
        return False  # Returns False if they aren't


# Testing

# Example Cases Given
print("Example Cases\n")

# No Options Enabled
print("No Options Enabled\n")

print(is_palindrome("racecar"))
print(is_palindrome("Racecar"))
print(is_palindrome("12-3-21"))
print(is_palindrome("12-321"))
print(is_palindrome("nurses run"))
print(is_palindrome("Yo, banana boy"))

# Option A Enabled
print("\nOption A Enabled\n")

print(is_palindrome(string="racecar", case_insensitive=True))
print(is_palindrome(string="Racecar", case_insensitive=True))
print(is_palindrome(string="12-3-21", case_insensitive=True))
print(is_palindrome(string="12-321", case_insensitive=True))
print(is_palindrome(string="nurses run", case_insensitive=True))
print(is_palindrome(string="Yo, banana boy", case_insensitive=True))

# Option B Enabled
print("\nOptions B Enabled\n")

print(is_palindrome(string="racecar", whitespace_insensitive=True))
print(is_palindrome(string="Racecar", whitespace_insensitive=True))
print(is_palindrome(string="12-3-21", whitespace_insensitive=True))
print(is_palindrome(string="12-321", whitespace_insensitive=True))
print(is_palindrome(string="nurses run", whitespace_insensitive=True))
print(is_palindrome(string="Yo, banana boy", whitespace_insensitive=True))

# Option C Enabled
print("\nOptions C Enabled\n")

print(is_palindrome(string="racecar", ignore_punctuation=True))
print(is_palindrome(string="Racecar", ignore_punctuation=True))
print(is_palindrome(string="12-3-21", ignore_punctuation=True))
print(is_palindrome(string="12-321", ignore_punctuation=True))
print(is_palindrome(string="nurses run", ignore_punctuation=True))
print(is_palindrome(string="Yo, banana boy", ignore_punctuation=True))

# All options Enabled
print("\nAll Options Enabled\n")

print(is_palindrome(string="racecar", case_insensitive=True, whitespace_insensitive=True, ignore_punctuation=True))
print(is_palindrome(string="Racecar", case_insensitive=True, whitespace_insensitive=True, ignore_punctuation=True))
print(is_palindrome(string="12-3-21", case_insensitive=True, whitespace_insensitive=True, ignore_punctuation=True))
print(is_palindrome(string="12-321", case_insensitive=True, whitespace_insensitive=True, ignore_punctuation=True))
print(is_palindrome(string="nurses run", case_insensitive=True, whitespace_insensitive=True, ignore_punctuation=True))
print(is_palindrome(string="Yo, banana boy", case_insensitive=True, whitespace_insensitive=True,
                    ignore_punctuation=True))  # Also due to PEP8's 120 characters a line limit

# Checking whitespace_insensitive and ignore_punctuation
print("\n\nChecking whitespace_insensitive and ignore_punctuation\n")

# The following line checks if all whitespace is removed
if is_palindrome(string="race\t\n\r\f\vcar", whitespace_insensitive=True):
    print("whitespace_insensitive removes tabs, new lines, carriage returns, form feeds, and vertical tabs")
    # The line above prints the success message

# The following line checks if all symbols are removed
if is_palindrome(string="""taco`~!@#$%^&*()-_+=[{}]:;'",<>./?cat""", ignore_punctuation=True):
    print("ignore_punctuation removes every non-alphanumeric character on my keyboard")
    # The line above prints the success message

# Error Cases
print("\n\nError Cases")

# Test if passing in an int, float, list, boolean, dictionary, or tuple for the string raises an error
print("\nTesting Input for error handling\n")

try:
    print(is_palindrome(12343234))
except TypeError as e:
    print(f"Expected TypeError: {e}")
try:
    print(is_palindrome(12890.243988))
except TypeError as e:
    print(f"Expected TypeError: {e}")
try:
    print(is_palindrome(["racecar"]))
except TypeError as e:
    print(f"Expected TypeError: {e}")
try:
    print(is_palindrome(True))
except TypeError as e:
    print(f"Expected TypeError: {e}")
try:
    print(is_palindrome({"Color": "Cyan"}))
except TypeError as e:
    print(f"Expected TypeError: {e}")
try:
    print(is_palindrome((1, 2, 3)))
except TypeError as e:
    print(f"Expected TypeError: {e}")

# Testing if passing in an int, float, string, list, dictionary, or tuple instead of a boolean for the options raises
# an error
print("\nTesting Options for error handling\n")

try:
    print(is_palindrome(string="Radar", case_insensitive=184.5))  # Float
except TypeError as e:
    print(f"Expected TypeError: {e}")
try:
    print(is_palindrome(string="taco cat", whitespace_insensitive=80243))  # Int
except TypeError as e:
    print(f"Expected TypeError: {e}")
try:
    print(is_palindrome(string="civic,", ignore_punctuation=["Pancake"]))  # List
except TypeError as e:
    print(f"Expected TypeError: {e}")
try:
    print(is_palindrome(string="taco cat", whitespace_insensitive="coffee", ignore_punctuation="tea"))  # String
except TypeError as e:
    print(f"Expected TypeError: {e}")
try:
    print(is_palindrome(string="Level", case_insensitive={"Color": "Cyan"}, ignore_punctuation="Water"))  # Dictionary
except TypeError as e:
    print(f"Expected TypeError: {e}")
try:
    print(is_palindrome(string="Rain", case_insensitive=(1, 2, 3), ignore_punctuation=True))  # Tuple
except TypeError as e:
    print(f"Expected TypeError: {e}")
try:
    print(is_palindrome(string="Jackpot", case_insensitive=7, whitespace_insensitive=7, ignore_punctuation=7))
except TypeError as e:
    print(f"Expected TypeError: {e}")

