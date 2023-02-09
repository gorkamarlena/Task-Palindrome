# function which return reverse of a string
def is_palindrome(value):
    value = ''.join(value.split())

#  update the old value with a new value
    value = value.replace('.', '')
  
  #convert string to lowercase
    value = value.lower()
  
  #reverse the string
    return value == value[::-1]

print(is_palindrome(input('Enter the value: ')))