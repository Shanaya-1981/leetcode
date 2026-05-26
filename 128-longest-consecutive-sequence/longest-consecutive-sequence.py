class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        longest = 0
        for current_no in set_nums:
            length = 1
            next_no = current_no + 1
            previous_no = current_no - 1
            if previous_no not in set_nums:
                while next_no in set_nums:
                    length += 1
                    next_no += 1
                longest = max(longest, length)
        return longest