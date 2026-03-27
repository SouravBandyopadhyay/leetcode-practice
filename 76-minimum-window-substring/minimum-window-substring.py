from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        target_counts = defaultdict(int)
        for char in t:
            target_counts[char] += 1

        required = len(target_counts)
        formed = 0
        window_counts = defaultdict(int)
        left = 0
        min_len = float("inf")
        result = ""

        for right in range(len(s)):
            char = s[right]
            window_counts[char] += 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            while formed == required and left <= right:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    result = s[left : right + 1]

                left_char = s[left]
                window_counts[left_char] -= 1
                if (
                    left_char in target_counts
                    and window_counts[left_char] < target_counts[left_char]
                ):
                    formed -= 1
                left += 1

        return result
