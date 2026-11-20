class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = 0
        left = 0
        ans = float("-inf")

        for right in range(len(nums)):
            window_sum += nums[right]

            if right - left + 1 == k:
                window_avg = window_sum / k
                ans = max(ans, window_avg)

                window_sum -= nums[left]
                left += 1

        return ans