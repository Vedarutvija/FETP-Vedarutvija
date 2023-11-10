<<<<<<< HEAD
# pattern.py
def generate_pattern(n):
    input_string = "FORMULAQSOLUTIONS"
    pattern_output = ""

    for i in range(n // 2 + 1):
        for space in range(n - i - 1):
            pattern_output += ""
        start_index = i
        end_index = i + (2 * i) + 1
        for char_index in range(start_index, end_index):
            pattern_output += input_string[char_index % len(input_string)]
        pattern_output += "\n"

    for i in range(n // 2, 0, -1):
        for space in range(n - i):
            pattern_output += ""

        start_index = n // 2 + 1 - i
        end_index = start_index + (2 * i) - 1
        for char_index in range(start_index, end_index):
            pattern_output += input_string[char_index % len(input_string)]

        pattern_output += "\n"

    return pattern_output
=======

>>>>>>> origin/master
