class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            current = nums[i]
            diff = target - current
            for j in range(i + 1, len(nums)):
                if nums[j] == diff:
                    return [i, j]
        return None

    def twoSumFaster(self, nums, target):
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in nums_dict and nums_dict[diff] != i:
                return [i, nums_dict[diff]]
            else:
                continue
        return None
                
solu = Solution()
print solu.twoSum([2, 3, 8, 4, 5], 12)
print solu.twoSumFaster([2, 3, 8, 4, 5], 12)