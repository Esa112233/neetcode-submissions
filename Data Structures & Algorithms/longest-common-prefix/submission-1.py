class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        j = 0

        for i in range(len(prefix)):
            for string in strs:
                if len(string) == i or string[i] != prefix[i]:
                    return prefix[:i]
                j += 1
        return prefix