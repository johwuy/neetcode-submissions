class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left = 0
        counter = Counter()
        for index, char in enumerate(s):
            counter[char] += 1
            most_common_count = counter.most_common(1)[0][1]
            while (index - left + 1) - most_common_count > k:
                counter[s[left]] -= 1
                left += 1
            result = max(result, index - left + 1)
        return result