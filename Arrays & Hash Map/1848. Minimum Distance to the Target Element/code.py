class Solution:
  def getMinDistance(self,  nums: List[int], target: int, start: int) -> int:
    minNum = float('inf')
    
    for i in range(len(nums)):
      if nums[i] == target:
        minNum = min(minNum, abs(start - i))
    return minNum