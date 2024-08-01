class Solution(object):
    def findClosestNumber(self, nums):
       closest = float('inf')
       for num in nums:
        if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
            closest = num 
       return closest 
        