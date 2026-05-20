class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Create left list with same length as nums
        left = [1] * len(nums)

        # Loop starting from index 1 (index 0 stays 1, nothing to its left)
        left[0] = 1
        for i in range(1, len(nums)):

            # Each position = previous left value × previous nums value
            left[i] = left[i-1] * nums[i - 1]
            # print(left)

        #Create right list which should have length similar to the nums
        right = [1] * len(nums)

        right[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
            # print(right)


        #then we multiply both left and right and return result
        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[i])
        return result
    