class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = list()
        n = len(nums)
        nums.sort()
        print(nums)
        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == num:
                continue

            j, k = i + 1, n - 1
            while j < k:
                threeSum = num + nums[j] + nums[k]
                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    result.append([num, nums[j], nums[k]])
                    j +=1 
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return result
