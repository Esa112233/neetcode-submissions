class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        tracker = {}

        for char in strs:
            sorted_str = "".join(sorted(char))
            if sorted_str not in tracker:
                tracker[sorted_str] = []
                tracker[sorted_str].append(char)
                continue
                
            tracker[sorted_str].append(char)

        answer = []

        for key, value in tracker.items():
            answer.append(value)

        return answer
