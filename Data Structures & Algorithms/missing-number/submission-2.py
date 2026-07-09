class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=len(nums)
        a=s*(s+1)//2
        for i in range(s):
            a-=nums[i]
        if a!=0:
            return abs(a)
        else:
            return 0