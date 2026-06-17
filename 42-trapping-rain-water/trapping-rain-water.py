class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        left_max = [0] * size
        right_max = [0] * size
        current_max_left = 0
        current_max_right = 0
        water = 0

        for left in range(size):
            current_max_left = max(current_max_left, height[left])
            left_max[left] = current_max_left

        for right in range(size-1, -1, -1):
            current_max_right = max(current_max_right, height[right])
            right_max[right] = current_max_right

        # print(left_max)
        # print(right_max)

        for i in range(size):
            water += min(left_max[i], right_max[i]) - height[i]

        # print(water)
        # print(len(water))

            
        return water