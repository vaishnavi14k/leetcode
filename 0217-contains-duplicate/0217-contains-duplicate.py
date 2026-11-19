class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        op=False
        seen=set()
        for num in nums:
            if num in seen:
                op=True
            else:
                seen.add(num)
        return op