class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left = 0
        right = 0
        current_subsequent_letters = set()
        max_length = 0
        while right < len(s):
            if s[right] in current_subsequent_letters:
                current_subsequent_letters.remove(s[left])
                left += 1

            else:
                current_subsequent_letters.add(s[right])
                current_length = len(current_subsequent_letters)
                max_length = max(current_length, max_length)
                right += 1
        return max_length
            