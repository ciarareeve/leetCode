import math
from collections import Counter

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        int_list = []

        if x < 0: return False

        while x > 0:
            int_list.append(x % 10)
            x = x/10
        if (len(int_list)%2 == 1):
            mid = (len(int_list)/2) 
            int1 = int_list[: mid]
            int2= int_list[mid+1:]
        else:
            mid = (len(int_list)/2)
            int1 = int_list[: mid]
            int2= int_list[mid:]

        reversed_list = list(reversed(int2))
        
        if reversed_list == int1:
            return True

                

                
            