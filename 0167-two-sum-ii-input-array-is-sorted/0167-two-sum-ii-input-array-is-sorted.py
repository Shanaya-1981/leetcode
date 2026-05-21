class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
       
        left =  0
        right = len(numbers) - 1

        while left < right:

            # calculate sum of both pointers
            current_total = numbers[left] + numbers[right]
            if current_total == target:
                return [left + 1, right + 1]

            if current_total > target:
                right -= 1
        
            if current_total < target:
                left += 1
