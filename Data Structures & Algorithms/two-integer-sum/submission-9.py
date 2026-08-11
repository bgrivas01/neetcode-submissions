class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for index, value in enumerate(nums):
            find = target - value
            if find in hashMap and hashMap.get(find) != index:
                return [ hashMap.get(find), index]
            hashMap[value] = index
        return []