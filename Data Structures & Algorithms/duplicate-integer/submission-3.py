class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()

        k = 0
        
        for i in range(1, len(nums)):
            if nums[k] == nums[i]:
                return True
            k += 1
        return False