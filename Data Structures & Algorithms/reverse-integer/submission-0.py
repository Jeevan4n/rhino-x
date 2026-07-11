class Solution:
    def reverse(self, x: int) -> int:
        curr=abs(x)
        if x<0:
            sign=-1
        else:
            sign=1
        c=0

        while curr>0:
            a=curr%10
            c=c*10+a
            curr=curr//10
        c=c*sign
        if c>(2**31 - 1) or c<(-2**31):
            return 0
        return c