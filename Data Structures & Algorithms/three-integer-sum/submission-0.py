class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        ans = []
        for i in range(len(nums)):
           for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if(nums[i]+nums[j]+nums[k]== target):
                        temp = [nums[i],nums[j],nums[k]]
                        temp = sorted(temp)
                        if temp not in ans:
                            ans.append([nums[i],nums[j],nums[k]])

        return ans
