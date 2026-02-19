class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_list = []
        count = 0
        strings = []
        max_count_list = []

        if not s:
            return 0
        
        for i in s:
            if i not in unique_list:
                unique_list.append(i)
                count += 1

            else:
                max_count_list.append(count)

                index = unique_list.index(i)
                unique_list = unique_list[index+1:]
                unique_list.append(i)
                count = len(unique_list)
                
        max_count_list.append(count)
        return max(max_count_list)
    
#sol = Solution()
#user_input = input('Provide input')
#result = sol.lengthOfLongestSubstring(user_input)
#
#print(result)
