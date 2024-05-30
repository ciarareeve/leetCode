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
            print("in odd num section")
            mid = (len(int_list)/2) 
            int1 = int_list[: mid]
            int2= int_list[mid+1:]
        else:
            print("in even num section")
            mid = (len(int_list)/2)
            int1 = int_list[: mid]
            int2= int_list[mid:]

        reversed_list = list(reversed(int2))
        
        print (int1, reversed_list)

        new = [i for i, j in zip(int1, reversed_list) if i ==j]
        if len(new) == len(int1) == len(reversed_list):
            return True

                
            
