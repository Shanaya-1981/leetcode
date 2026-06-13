class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size_of_nums = len(nums)
        left = [1] * size_of_nums
        right = [1] * size_of_nums

        left[0] = 1
        for left_array in range(1, len(nums)):
            left[left_array] = left[left_array-1] * nums[left_array-1]

        right[-1] = 1
        for right_array in range(len(nums)-2, -1, -1):
            right[right_array] = right[right_array + 1] * nums[right_array + 1]
        # print(right)

        result = [left[i] * right[i] for i in range(size_of_nums)]
        # print(result)

        # print(left)


        return result

