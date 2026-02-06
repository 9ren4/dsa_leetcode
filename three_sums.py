class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = 0
        final_result = []
        n = -1
        m = -2
        for i in nums:
            mini_list = []
            if i >= 0:
                break
            else:
                result = i + nums[n] + nums[m]
                if result == 0:  
                    mini_list.append([i, nums[n], nums[n]])
                    n -= 1
                    m -= 1
                    final_result.append(mini_list)     

                else:
                    n -= 1
                    m -= 1 
                    continue

        return final_result            
    

# ---- user input + function call ----
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

solution = Solution()
output = solution.threeSum(nums)

print("Triplets that sum to zero:")
print(output)
