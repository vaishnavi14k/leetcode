class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen=[]
        ans=[]
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in seen:
                ans.append(i)
                ans.append(seen.index(complement))
            else:
                seen.append(nums[i])
        return ans

                
