class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        longest_pair = 0
        for no in set_nums:
            previous_no = no -1
            next_no = no + 1
            current_pair_length = 1
            if previous_no not in set_nums:
                while next_no in set_nums:
                    next_no += 1
                    current_pair_length +=1
                longest_pair = max(current_pair_length, longest_pair)
        return longest_pair