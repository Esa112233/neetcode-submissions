class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = list(s)

        longest = 0
        substr = set()

        L = 0

        for R in string:

            if R not in substr:
                substr.add(R)
            else:
                while R in substr:
                    substr.remove(string[L])
                    L += 1
                substr.add(R)
            longest = max(longest, len(substr))  
        return longest


