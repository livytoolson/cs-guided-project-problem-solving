"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.

What if n is:
    * a string -- if it's not an int, force to int with int()
    * a float -- if it's not an int, force to int with int()
    * a negative -- return empty list
    * complex numbers? -- don't need to deal with this

What if the list 
    * Is empty? -- no special rules
"""


def last(a, n):
    # Make sure n is an int
    try:
        n = int(n)
    
    except ValueError as e: # e becomes a variable with information in it about the error
        # print(e) 
        return "invalid number"

    # Check if n is positive
    if n <= 0:
        return []

    # Make sure n is not too large
    if n > len(a):
        return "invalid"

    # Get the last n elements from the list

    """
    result = []

    You could use a for loop --
    # Loop n times
    for _ in range(n):

        # Pop the value off the end of the list 
        val = a.pop()

        # Insert the value at the front of the result list
        result.insert(0, val)

    return result
    """

    # You could also use slicing -- 
    # Make me a new list starting from the nth of the end all the way to the end 
    return a[-n:]

print(last([4, 3, 9, 9, 7, 6], 3)) # ➞ [9, 7, 6]
print(last([1, 2, 3, 4, 5], 7)) # ➞ "invalid"
print(last([1, 2, 3, 4, 5], 0)) # ➞ []
print(last([4, 2, 9, 9, 7, 6], "livy"))
print(last([4, 2, 9, 9, 7, 6], -7))
