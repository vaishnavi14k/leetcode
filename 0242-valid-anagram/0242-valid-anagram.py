class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one={}
        two={}
        for num in s:
            one[num]=one.get(num,0)+1
        for num in t:
            two[num]=two.get(num,0)+1
        if one==two:
            return True
        else:
            return False