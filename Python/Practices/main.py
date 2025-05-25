class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if len(x) % 2 == 0:
            flag = True
            for i in range(len(x) // 2):
                if x[i] == x[-i -1]:
                    continue
                else:
                    flag = False
        if len(x) % 2 == 1:
            flag = True
            for i in range((len(x) - 1) // 2):
                if x[i] == x[-i -1]:
                    continue
                else:
                    flag = False
        return flag
