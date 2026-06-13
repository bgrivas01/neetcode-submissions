class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for x in range(len(nums)):
            if nums[x] >0:
                break
            if x>0 and nums[x] == nums[x-1]:
                continue
            left = x+1
            right = len(nums)-1
            while left< right:
                if nums[x] + nums[left]+nums[right] < 0:
                    left+=1
                elif nums[x] + nums[left]+nums[right] > 0:
                    right-=1
                else:
                    res.append([nums[x],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left] == nums[left-1]:
                        left+=1


        return res