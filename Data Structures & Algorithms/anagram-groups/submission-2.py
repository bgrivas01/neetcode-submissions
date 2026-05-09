class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        def isAnagram(word1, word2):
            if len(word1) != len(word2): #Check if length are the same
                return False

            sMap, tMap = {}, {}

            for x in range(len(word1)):
                sMap[word1[x]] = 1 + sMap.get(word1[x],0)
                tMap[word2[x]] = 1 + tMap.get(word2[x],0)
            return sMap == tMap
        
        
        for word in strs:
            found = False
            if len(out) == 0:  #if out is empty then add the first word in to a list and then add that as a "sublist" to the list we will be returning
                newList = [word]
                out.append(newList)
            else:
                for y in range(len(out)):
                    if isAnagram(out[y][0], word):
                        out[y].append(word)
                        found = True
                        break
                if not found:
                    newList = [word]
                    out.append(newList)
        

            
        return out