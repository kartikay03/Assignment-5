# Python code to reverse a string
def reverse(string):
    string = "".join(reversed(string))
    return string
s = "Python"
print("The original string is : ", end="")
print(s)
print("The reversed string(using reversed) is : ", end="")
print(reverse(s))
