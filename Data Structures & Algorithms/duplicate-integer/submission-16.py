class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         hashset=set()
         for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
         return False
    print(hasDuplicate("", [1,2,3,3]))