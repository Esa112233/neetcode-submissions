class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        slowest_time = []
        ans = 0
        sorted_list = []
        for i in range(len(position)):
            sorted_list.append((position[i], speed[i]))
        sorted_list.sort(reverse=True)


        for i in range(len(sorted_list)):
            time = (target-sorted_list[i][0])/sorted_list[i][1]

            if not slowest_time:
                slowest_time.append(time)
                ans += 1
            else:
                if time > slowest_time[-1]:
                    ans += 1
                    slowest_time[-1] = time
        return ans

