class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
    
        left = 0
        counting_s = {}
        max_length = 0
        right = 0

        while right < len(s):
        
            if s[right] in counting_s:
                counting_s[s[right]] += 1
            else:
                counting_s[s[right]] = 1


            while (right - left + 1) - max(counting_s.values()) > k:
                counting_s[s[left]] -= 1
                left += 1
                
            # update max_length
            max_length = max(max_length, right - left + 1)

            # move right forward
            right += 1
        return max_length