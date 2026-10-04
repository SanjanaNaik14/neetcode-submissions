class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs={}
        for char in s:
            if char not in hashs:
                hashs[char]=1
            else:
                hashs[char]=hashs[char]+1
        hasht={}
        for cha in t:
            if cha not in hasht:
                hasht[cha]=1
            else:
                hasht[cha]=hasht[cha]+1
        return hashs==hasht
    isAnagram(" ","racecar", "carrace")