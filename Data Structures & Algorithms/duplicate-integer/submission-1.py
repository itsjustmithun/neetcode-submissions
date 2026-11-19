class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_sets = set(nums)
        return len(check_sets) != len(nums)