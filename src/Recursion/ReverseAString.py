def reverse_a_string(str):
    if str == '':
        return str

    return str[-1] + reverse_a_string(str[:-1])

print(reverse_a_string('cunt'))