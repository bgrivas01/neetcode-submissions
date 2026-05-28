class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        output.append([strs[0]])
        
        for x in range(1, len(strs)):
            found = False
            for y in range(0, len(output)):
                if self.isAnagram( strs[x], output[y][0]):
                    output[y].append(strs[x])
                    found = True
            if not found:
                output.append([strs[x]])

        return output


    def isAnagram(self, word1, word2): #this function is O(nlogn)
        if len(word1)!= len(word2):
            return False
        return sorted(word1) == sorted(word2)