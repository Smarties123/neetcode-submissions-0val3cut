class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = 0
        hash_table = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            

            if nums[i] in hash_table:
                return [hash_table[nums[i]], i]
            hash_table[complement] = i