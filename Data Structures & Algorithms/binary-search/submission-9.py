class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Start with the full search range
        l = 0
        r = len(nums) - 1

        # Keep searching while the range is valid
        while l <= r:
            # Middle index
            m = (l + r) // 2

            # Found target
            if nums[m] == target:
                return m

            # Target is on the right side
            elif nums[m] < target:
                l = m + 1

            # Target is on the left side
            else:
                r = m - 1

        # Target was not found
        return -1