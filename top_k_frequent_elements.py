class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        groups = {}
        result = []
        for i in nums:
            if i not in groups:
                groups[i] = []

            groups[i].append(i)

        for i in range(k):
            max_key = None
            max_count = -1
            for key,v in groups.items():
                if len(v) > max_count:
                    max_count = len(v)
                    max_key = key

            result.append(max_key)
            groups.pop(max_key)

        return result

        


        
