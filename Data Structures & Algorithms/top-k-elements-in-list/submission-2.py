class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencies = {}

        for i in range(len(nums)):
            if nums[i] not in frequencies:
                frequencies[nums[i]] = 1
            else:
                frequencies[nums[i]] += 1

        highest_value = []
        
        while k != 0:
            max_key = max(frequencies, key=frequencies.get)
            highest_value.append(max_key)
            frequencies.pop(max_key)
            k -= 1
        
        return highest_value