class Solution:
    def reverseBits(self, n: int) -> int:
        a=list(bin(n)[2:].zfill(32))
        l=0
        r=len(a)-1
        while l<r:
            a[l],a[r]=a[r],a[l]
            l+=1
            r-=1
        c="".join(a)
        z=int(c,2)
        return z



        