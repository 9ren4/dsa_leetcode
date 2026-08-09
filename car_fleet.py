class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = {}
        result = 0
        last_time = 0
        for i, j in zip(position, speed):
            dic[i] = j

        sorted_dict = dict(sorted(dic.items(),reverse = True))
        for pos,sped in sorted_dict.items():
            time = (target-pos)/sped
            if time > last_time:
                result += 1
                last_time = time

        return result