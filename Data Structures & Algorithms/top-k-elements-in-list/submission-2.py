class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      hashmap={}
      for i in range(len(nums)):
            hashmap[nums[i]]=1+hashmap.get(nums[i],0)
        
      valuelist=list(hashmap.values())
      valuelist.sort()
      valuelist.reverse()
      freq=0
      topfreq=[]
      while freq<k:
            topfreq.append(valuelist[freq])
            freq+=1
      op=[]
      for key,values in hashmap.items():
            if values in topfreq:
                op.append(key)
      return op
    