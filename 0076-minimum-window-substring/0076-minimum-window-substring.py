class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
       
        t_count = {}
        for char in t:
                t_count[char] = t_count.get(char, 0) + 1

        window_count = {}
        left = 0
        right = 0
        result = ""

        while right < len(s):
           
            window_count[s[right]] = window_count.get(s[right], 0) + 1

            while all(window_count.get(char, 0) >= t_count[char] for char in t_count):
                
                current_window = s[left:right + 1]
                if result == "" or len(current_window) < len(result):
                    result = current_window
              
                window_count[s[left]] -= 1
               
                left += 1

      
            right += 1

        return result