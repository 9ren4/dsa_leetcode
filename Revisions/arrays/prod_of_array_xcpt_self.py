#I coded this whole thing just learning the concept without seeing any prior code, but the complexities are real bad althought it works
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = []
        postfix = []
        result = []
        multiple = 1
        second_multiple = 1
        for i in nums:
            multiple *= i
            prefix.append(multiple)

        for i in reversed(nums):
            second_multiple *= i
            postfix.insert(0,second_multiple)

        for i in range(len(nums)):
            if i == 0:
                result.append(postfix[1])
            elif i == len(nums) - 1:
                result.append(prefix[len(nums)-2])
            else:
                result.append(prefix[i-1]*postfix[i+1])

        return result
#This is the optimized version of the above code, which is O(n) time and O(1) space complexity

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)

        # Prefix products
        prefix = 1

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # Postfix products
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result