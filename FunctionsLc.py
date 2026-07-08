#2544.Alternating Digit Sum
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n1=str(n)
        sum=0
        diff=0
        for i in range(len(n1)):
            if i%2==0:
                sum+=int(n1[i])
            else:
                diff-=int(n1[i])
        return sum+diff
#2553. Separate the Digits in an Array task
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr=[]
        for num in nums:
            for i in str(num):
                arr.append(int(i))
        return arr
        
