class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={}
        ans=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        ordered=sorted(freq,key=freq.get,reverse=True)
        return ordered[:k]