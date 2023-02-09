x = input('Enter the value: ')

def is_palindrome(text):
    text = "".join([x for x in text.lower() if x.isalnum()])
    return text == text[::-1]

print(is_palindrome(x))





