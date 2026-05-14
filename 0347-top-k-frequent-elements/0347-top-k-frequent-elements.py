class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        count_nums = {}
        for no in nums:
            if no not in count_nums:
                count_nums[no] = 1
            else:
                count_nums[no] += 1

        return sorted(count_nums, key=count_nums.get, reverse=True)[:k]
        # print(count_nums)
