class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        multiply = 1
        multiply_2 = 1
        
        for i in nums:
            multiply *= i
        count_zeroes = nums.count(0)
        if count_zeroes == 1 :
            for k in nums:
                if k != 0:
                    multiply_2 *= k

            

        for index,j in enumerate(nums):

            if count_zeroes > 1:
                result = [0] * len(nums)
                continue
            elif j != 0: 
                x = int(multiply/j)
                if x != 0:
                    result.append(x)
                else:
                    result.append(abs(x))
                continue
            else:
                result.append(multiply_2)

        return result
            
 