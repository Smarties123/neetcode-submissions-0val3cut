class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        arr_map = {} # eg: arr_map[number] = index  

        for i, n in enumerate(nums):
            difference = target - n

            if difference in arr_map:
                return [arr_map[difference], i]
            
            arr_map[n] = i
        


