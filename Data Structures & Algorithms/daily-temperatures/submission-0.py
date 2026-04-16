class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)-1):
            currday = temperatures[i]
            count = 1
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > currday:
                    break
                count += 1
                if j + 1 == len(temperatures):
                    count = 0
            res.append(count)
        res.append(0)
        return res