class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        freq={}
        n=len(nums)
        ans=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
            if freq[num]>n/3:
                if num not in ans:
                    ans.append(num)
                

        return ans