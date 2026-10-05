#This code is written by me, and it works fine but the code is longer and not effiecient, so I will try to optimize it and make it shorter and more efficient code writing
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_num = set(nums)
        count = 0
        i_prev = 0
        result = 0
        if nums == []:
            return 0
        for i in set_num:
            i_prev = i -1
            if i_prev not in set_num:
                count = 1
                while True:
                    i += 1
                    if i in set_num:
                        count += 1
                        result = max(count,result)
                    else:
                        break
        if result == 0:
            return 1
        else:
            return result
#This is the optimized version of the above code
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_num = set(nums)
        result = 0

        for i in set_num:
            if i - 1 not in set_num:
                count = 1

                while i + count in set_num:
                    count += 1

                result = max(count, result)

        return result
