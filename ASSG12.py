"""12. Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed."""


def is_palindrome(word):
    rev=word[::-1]
    if rev ==word:
        print("palindrome")
    else:
        print("Non palindrome")


is_palindrome("helh")