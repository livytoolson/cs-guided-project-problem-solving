"""
Strings are immutable

Challenge #7:

Given a string of lowercase and uppercase alpha characters, write a function
that returns a string where each character repeats in an increasing pattern,
starting at 1. Each character repetition starts with a capital letter and the
rest of the repeated characters are lowercase. Each repetition segment is
separated by a `-` character.

Examples:
- repeat_it("abcd") -> "A-Bb-Ccc-Dddd"
- repeat_it("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
- repeat_it("cwAt") -> "C-Ww-Aaa-Tttt"

Questions:
    * What if there are non-alphabetic character in the string? Including space?
        * We don't need to worry about this
    * What if we get an empty string?
        * Return an empty string
"""
def repeat_it(input_str):
    # check for empty string
    if input_str == "":
        return ""

    # convert the input string to a list
    input_list = list(input_str)

    result_list = []

    # loop through list
    for reps, char in enumerate(input_list):

        # print(reps, char)

        # repeat the character
        """
        repeated_char = ""

        for _ in range(reps + 1):
            repeated_char += char
        """

        repeated_char = char * (reps + 1)

        # capitalize the new string
        repeated_char = repeated_char.capitalize()

        # print(repeated_char)

        # add items to result list
        result_list.append(repeated_char)

    # join result list with -
    result_str = "-".join(result_list)

    # return the string
    return result_str

print(repeat_it("abcd"))
print(repeat_it("RqaEzty"))
print(repeat_it("cwAt"))
