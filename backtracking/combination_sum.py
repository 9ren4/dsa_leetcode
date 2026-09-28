class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []

        def backtrack(index, current, current_sum):
            if current_sum == target:
                results.append(current.copy())
                return

            if index >= len(candidates) or current_sum > target:
                return

            current.append(candidates[index])
            backtrack(index, current, current_sum + candidates[index])

            current.pop()
            backtrack(index + 1, current, current_sum)

        backtrack(0, [], 0)

        return results