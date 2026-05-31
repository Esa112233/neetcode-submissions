class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        length = len(temperatures)
        for i in range(length):
            count = 1
            while i < length:
                if i + count == length:
                    result.append(0)
                    break
                if temperatures[i] < temperatures[i+count]:
                    result.append(count)
                    break
                else:
                    count += 1
        return result


