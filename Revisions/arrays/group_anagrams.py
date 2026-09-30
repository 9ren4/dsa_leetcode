class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       groups = {}
       result = []
       sorted_word = []
       for i in strs:
        sorted_words = "".join(sorted(i))
        sorted_word.append(sorted_words)
       for ind,val in enumerate(sorted_word):
        if val not in groups:
            groups[val] = [ind]
        else:
            groups[val].append(ind)
       for indexes in groups.values():
        group = []
        for index in indexes:
            group.append(strs[index])
        result.append(group)

       return result  


                   
        