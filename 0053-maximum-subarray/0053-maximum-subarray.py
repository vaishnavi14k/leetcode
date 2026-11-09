class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum=0
        max_sum=nums[0]
        for num in nums:
            current_sum=current_sum+num
            current_sum=max(num,current_sum)
            max_sum=max(current_sum,max_sum)

        return max_sum