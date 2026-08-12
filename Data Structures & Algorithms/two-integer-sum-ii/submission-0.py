class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        numbers_map = {} # numbers_map[number] = index

        for i, n in enumerate(numbers):
            difference = target - n

            if difference in numbers_map and numbers_map[difference] < i:
                return [numbers_map[difference] + 1, i + 1]
            
            numbers_map[n] = i

            
        
        