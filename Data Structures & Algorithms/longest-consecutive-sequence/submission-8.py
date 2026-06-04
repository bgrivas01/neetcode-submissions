class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        exists = True
        res = 1
        newres = 1
        for x in range(len(nums)):
            if nums[x]-1 not in nums:
                exist = False
                y=nums[x]
                newres =1
                while exist == False:
                    if y+1 in nums:
                        newres+=1
                        y+=1
                    else:
                        if newres > res:
                            res = newres
                        exist = True

        return res