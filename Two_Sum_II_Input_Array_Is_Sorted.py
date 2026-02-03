class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i,v in enumerate(numbers):
            search_number = target - v
            if search_number in numbers and numbers.index(search_number) != i:
                return  sorted([i + 1, numbers.index(search_number) + 1])