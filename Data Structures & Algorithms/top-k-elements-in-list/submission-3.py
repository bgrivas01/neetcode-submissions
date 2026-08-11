class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for x in range(len(nums)+1)]
        count = {}

        for number in nums:
            count[number] = 1+count.get(number,0)
        for number, cnt in count.items():
            freq[cnt].append(number)

        res = []
        for x in range(len(freq)-1, 0,-1):
            for number in freq[x]:
                res.append(number)
                if len(res)==k:
                    return res