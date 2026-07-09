class Solution:
    def isPalindrome(self, s: str) -> bool:
        duplicateStr = "".join([i.lower() for i in s if i.isalnum()])
        left = 0
        right = len(duplicateStr) - 1
        while left < right:
            if duplicateStr[left] != duplicateStr[right]:
                return False
            left += 1
            right -= 1

        return True