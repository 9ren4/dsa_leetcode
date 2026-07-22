class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for index,value in enumerate(temperatures):
            found = False
            for i,j in enumerate(temperatures[index+1:]):
                if j > value:
                    result.append(i+1)
                    found = True
                    break
                if not found:
                    result.append(0)

            
        return result
