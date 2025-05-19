def is_palindrome(str):
    if len(str) == 1 or len(str) == 0:
        return True

    if str[1] == str[-1]:
        return is_palindrome(str[1:-1])

    return False

print(is_palindrome('racecar'))
print(is_palindrome('hello'))
