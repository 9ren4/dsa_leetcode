class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_word = sorted(s)
        second_word = sorted(t)
        if first_word == second_word:
            return True
        else:
            return False