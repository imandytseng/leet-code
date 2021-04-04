class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for first in range(len(nums) - 1):
            for second in range(first + 1, len(nums)):
                if nums[first] + nums[second] == target:
                    return [first, second]
        # Result: 32ms (73.45%), 13.5MB (48.08%)


class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, value in enumerate(nums):
            try:
                return [index, nums.index(target - value, index + 1)]
            except:
                pass
        # Result: 32ms (73.45%), 13.5MB (76.27%)


class BestFound(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for index, value in enumerate(nums):
            if value in d:
                return [index, d[value]]
            d[target-value] = index
        # Result: 24ms (99.10%), 13.5MB (76.27%)
