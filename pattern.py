def generate_pattern(n):
    input_string = "FORMULAQSOLUTIONS"
    pattern_output = ""
    last_row_chars = ""

    for i in range(n // 2 + 1):
        for space in range(n - i - 1):
            pattern_output += ""
        start_index = i
        end_index = i + (2 * i) + 1
        row_chars = ""
        for char_index in range(start_index, end_index):
            row_chars += input_string[char_index % len(input_string)]
        last_row_chars = row_chars
        pattern_output += row_chars + "\n"

    for i in range(n // 2, 0, -1):
        for space in range(n - i):
            pattern_output += ""

        start_index = n // 2 + 1 - i
        end_index = start_index + (2 * i) - 1
        for char_index in range(start_index, end_index):
            pattern_output += last_row_chars[char_index % len(last_row_chars)]

        pattern_output += "\n"

    return pattern_output

