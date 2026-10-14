class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self,nums):
        rob1,rob2 = 0,0
        for i in nums:
            max_rob = max(rob2+i,rob1)
            rob2 = rob1
            rob1 = max_rob
        return rob1