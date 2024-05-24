class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff = 0
        index_map = {}
        
        # index, value
        for i, j in enumerate(nums):
            diff = target - j
            if diff in index_map:
                return [index_map[diff], i]
            #if current num not in map, add it
            index_map[j] = i