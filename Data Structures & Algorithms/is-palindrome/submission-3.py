class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        filtered = [char for char in s if char.isalnum()]
        s = "".join(filtered).lower()
        left, right = 0, len(s) - 1
        print(s)

        for i in range(right+1):
            print(left, s[left])
            print(right, s[right])
            if left >= right:
                return True
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return False
        return True














