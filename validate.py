# re.search(pattern, string, flags=0)
"""
Pattern - The regular expression pattern you want to search:
    . - Any Character Except New Line
    * - 0 or More Repetitions
    + - 1 or More Repetitions
    ? - 0 or 1 Repetitions
    {3} - Exact Number of Repetitions
    {3,4} - Range of Numbers (Minimum, Maximum)
"""

import re

email = input("Enter your email: ").strip().lower()
    
if re.search(".+@.+\.edu", email):
    print("Valid email")
else:
    print("Invalid email")
 