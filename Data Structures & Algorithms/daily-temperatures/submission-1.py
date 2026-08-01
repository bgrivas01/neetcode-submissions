class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for x in range(len(temperatures)):
            for y in range(x+1, len(temperatures)):
                if temperatures[y] > temperatures[x]:
                    res.append(y-x)
                    break
            else:
                res.append(0) 
                    
        return res

