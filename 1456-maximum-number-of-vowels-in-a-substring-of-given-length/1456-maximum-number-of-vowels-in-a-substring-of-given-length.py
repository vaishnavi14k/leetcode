class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        max_ans = 0

        for right in range(len(s)):
            if s[right] in "aeiou":
                ans += 1

            if right - left + 1 == k:
                max_ans = max(max_ans, ans)

                if s[left] in "aeiou":
                    ans -= 1

                left += 1

        return max_ans