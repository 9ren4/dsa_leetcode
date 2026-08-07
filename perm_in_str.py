class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        s1_dic = {}
        for c in s1:
            s1_dic[c] = s1_dic.get(c,0)+1

        while r <= len(s2):
            s2_sub_dic = {}
            for i in s2[l:r]:
                s2_sub_dic[i] = s2_sub_dic.get(i,0)+1
            if s1_dic == s2_sub_dic:
                return True
            else:
                l += 1
                r += 1

        return False
