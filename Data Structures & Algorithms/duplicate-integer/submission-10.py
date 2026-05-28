class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()

        for x in range(0, len(nums)):
            if nums[x] in myset:
                return True
            else:
                myset.add(nums[x])
        return False