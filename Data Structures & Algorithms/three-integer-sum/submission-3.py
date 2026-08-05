class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=-nums[i]
            while j<k:
                curr=nums[j]+nums[k]
                if curr==target:
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1

                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1

                elif curr<target:
                    j+=1
                else:
                    k-=1
        return ans