class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        s_counter = Counter()

        required = len(t_counter)
        satisfied = 0

        left = 0
        best_left = 0
        best_len = float("inf")

        for right in range(len(s)):
            char = s[right]
            s_counter[char] += 1

            if char in t_counter and s_counter[char] == t_counter[char]:
                satisfied += 1

            while satisfied == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left

                char = s[left]
                s_counter[char] -= 1

                if char in t_counter and s_counter[char] < t_counter[char]:
                    satisfied -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_left:best_left + best_len]