class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcons=count=0
        for i in nums:
            if i==1:
                count+=1
                print(f"found 1 at position {i}")
            elif i==0 or i==len(nums)-1:
                maxcons=max(maxcons, count)
                count=0
        return max(maxcons, count)
            