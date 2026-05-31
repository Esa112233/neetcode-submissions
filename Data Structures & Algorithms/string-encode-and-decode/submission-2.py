class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes = []
        for string in strs:
            sizes.append(len(string))

        string = ""

        for index, size in enumerate(sizes):
            
            if index == len(sizes) - 1:
                string += str(size) + "#"
            else:
                string += str(size) + ","

        plainstr = "".join(strs)

        string+=plainstr

        return string


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        split = s.split('#', 1)

        sizes = split[0]
        sizes = sizes.split(',')
        string = split[1]
        result = []

        total_covered = 0
        for size in sizes:
            result.append(string[total_covered:total_covered + int(size):1])
            total_covered += int(size)
        
        return result



        pass
