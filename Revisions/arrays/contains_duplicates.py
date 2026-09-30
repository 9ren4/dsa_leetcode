class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_one = set(nums)
        if len(set_one) == len(nums):
            return False
        else:
            return True   
