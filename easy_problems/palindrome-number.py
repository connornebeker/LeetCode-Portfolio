class Solution:
    def isPalindrome(x: int) -> bool:
        x = str(x)
        y = x[::-1]
        if x == y:
            return True
        else:
            return False
    
    print(isPalindrome(12321))
