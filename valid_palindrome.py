class Solution:
    def isPalindrome(self, s: str) -> bool:
        strings = []
        for i in s:
            if i.isalnum():
                strings.append(i.lower())

        reversed_list = strings[::-1]

        if reversed_list == strings:
            return True

        else:
            return False