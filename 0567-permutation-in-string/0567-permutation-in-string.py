class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
   
    
        s1_count = {}
        for count in s1:
            if count not in s1_count:
                s1_count[count] = 1
            else:
                s1_count[count] += 1
        window_size = len(s1)
        if len(s2) < window_size:
            return False

        for char in range(len(s2)- window_size + 1):
            window = s2[char: char + window_size]
            s2_count = {}
            for i in window:
                if i not in s2_count:
                    s2_count[i] = 1
                else:
                    s2_count[i] += 1

            if s2_count == s1_count:
                return True

        return  False