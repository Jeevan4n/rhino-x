class Solution:
    def countBits(self, n: int) -> List[int]:
        a=[]
        for i in range(n+1):
            count=0
            num=i
            while num>0:
                if num%2==1:
                    count+=1
                num=num//2
            a.append(count)
        return a
        