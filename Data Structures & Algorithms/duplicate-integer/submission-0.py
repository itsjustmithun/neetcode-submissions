class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_sets = set(nums)
        print(check_sets)
        if len(check_sets) == len(nums):
            return False
        else:
            return True