def ispalindrome(s):
    return s == s[::-1]

print(ispalindrome(input("Enter string: ")))