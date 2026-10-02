"""
Top K Frequent Elements — Note
- My solution: Count frequencies → repeat k times → find the maximum frequency → add that number. O(n + k·m), worst case O(n²).
- Optimized: Use bucket sort → bucket[frequency] stores numbers with that frequency → traverse from highest frequency down. O(n).
- Key idea: Since a number can appear at most n times, frequency can be used as a bucket index.
"""
#My solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       count = {}
       result = []
       for number in nums:
        count[number] = count.get(number,0)+1
       for i in range(k):
        highest = max(count.values())
        for key,val in count.items():
            if val == highest:
                result.append(key)
                count.pop(key)
                break        

       return result


#Optimized solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = []
        result = []
        for num in nums:
            count[num] = count.get(num,0)+1
        for i in range(len(nums)+1):
            bucket.append([])
        for num,frequency in count.items():
            bucket[frequency].append(num)

        for i in range(len(nums),0,-1):
            for num in bucket[i]:
                result.append(num)

            if len(result) == k:
                return result