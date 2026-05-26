class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        known_no = set(nums)
        length_seq = 0
        max_length = 0
        for number in known_no:
            start_no = number - 1
            # print(f"start no is {start_no}")
            if start_no not in known_no:
                length_seq = 1
                next_no = number + 1
                # print(f"next no is {next_no}")
                while next_no in known_no:
                    next_no += 1
                    length_seq += 1
                max_length = max(max_length, length_seq)
        return max_length
