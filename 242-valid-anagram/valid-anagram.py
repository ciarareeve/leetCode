class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ana_dict = {}
        if s not in ana_dict:
            ana_dict[''.join(sorted(s))] = s
        if ''.join(sorted(t)) in ana_dict:
            return True
        else:
            return False

        