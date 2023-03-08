class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        nx = str(x)
        rn = []
        count = 0

        if x >= 0:
            for i in range(len(nx)-1, -1, -1):
                rn.append(nx[i])

            for i in range(len(nx)):
                if nx[i] == rn[i]:
                    count += 1

        if count == len(nx):
            return True

        else:
            return False