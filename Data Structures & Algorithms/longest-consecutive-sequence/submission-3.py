class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        starts = set()
        for num in nums:
            if num - 1 in nums:
                continue
            starts.add(num)
        
        max_length = 0
        for start in starts:
            length = 0
            while start + length in nums:
                length += 1
            max_length = max(max_length, length)
        return max_length