def palindrome(s):
    s = s.replace(" ","").lower()
    if s == s[::-1]:
        return True
    else:
        return False


print(palindrome('helleh'))
print(palindrome("liziL"))
print(palindrome("hello"))
print(palindrome("Able was I ere i saw elba"))
