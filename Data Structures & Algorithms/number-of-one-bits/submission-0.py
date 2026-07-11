class Solution:
    def hammingWeight(self, n: int) -> int:
        a=bin(n)[2:]
        count=0
        for ch in a:
            if ch=='1':
                count+=1
        return count
        