class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        window = set()
        left = 0
        for char in s:
            while char in window:
                window.remove(s[left])
                left += 1
            window.add(char)
            max_length = max(max_length, len(window))
        return max_length