class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in range(len(nums)+1)]#makes a 2d list the size of nums

        for x in range(0, len(nums)): #this is O(N)
            hashmap[nums[x]] = hashmap.get(nums[x],0)+1
        for n, c in hashmap.items():
            freq[c].append(n)

        response = []
        for i in range(len(freq) - 1,  0 , -1):#this gets it to increment down
            for n in freq[i]:
                response.append(n)
                if len(response) ==k:
                    return response
            
   