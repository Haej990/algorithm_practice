class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        length = len(s) // 2
        for i in range(length):
            alphabet = s[i]
            s[i] = s[-1-i]
            s[-1 - i] = alphabet