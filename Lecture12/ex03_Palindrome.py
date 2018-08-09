'''
Exercise03 - Palindrome Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

def isPalindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[len(s) - 1]:
        return False
    else:
        return isPalindrome(s[1:len(s) - 1])


def main():
    print("Is moon a palindrome?", isPalindrome("moon"))
    print("Is noon a palindrome?", isPalindrome("noon"))
    print("Is abcba a palindrome?", isPalindrome("abcba"))


main()
