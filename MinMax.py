class Solution:
    def getMinMax(self, arr):
        mini,maxi=float('inf'),float('-inf')
        for num in arr:
            if num<mini:
                mini = num
            if num>maxi:
                maxi = num
        return [mini, maxi]
