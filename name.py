import sys

"""
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("please enter name")
"""
"""
# Check for errors
if len(sys.argv) < 2:
    sys.exit("Error: Less than 2 arguments")
elif len(sys.argv) > 2:
    sys.exit("Error: More than 2 arguments")

# Print name tags
print("hello, my name is", sys.argv[1])
"""

if len(sys.argv) < 2:
    sys.exit("Error: Less than 2 arguments")

for arg in sys.argv[1:]:
    print("hello my name is", arg)