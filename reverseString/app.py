def reverseStr(str):
    return str[::-1]  # it functions as part of slice operator[start, stop, step]


print("This an app to reverse a string")
str = input("Enter a string to reverse it: ")
print("Ok your reversed string is:", reverseStr(str))
