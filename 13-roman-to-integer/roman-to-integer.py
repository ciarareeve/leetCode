class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        conversion_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        
        last_seen = s[0]
        total = conversion_map[last_seen]
        for i in s[1:]:
            if conversion_map[i] <= conversion_map[last_seen]:
                total += conversion_map[i]
            else:
                total += (conversion_map[i] - (2 * conversion_map[last_seen]))

            last_seen = i
                
        return total
            