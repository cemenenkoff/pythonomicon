def check_palindrome(s: str) -> bool:
    n = len(s)
    start = 0
    end = n - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


print("racecar", check_palindrome("racecar"))
print("racecars", check_palindrome("racecars"))
