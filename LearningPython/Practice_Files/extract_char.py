# how to extract char
str = "palindrome"
len_str = len(str)
for element in str:
    print(element, end=' ')
print("\n")


## palindrome function
def palindrome_func(str):
    for x in range(0, len(str)):
        if (str[x] != str[len(str) - x - 1]):
            return False
    return True

print(palindrome_func("palindrome"))
print(palindrome_func("racecar"))