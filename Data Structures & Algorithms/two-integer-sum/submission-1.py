class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # bruteforce
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # efficient
        seen = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in seen:
                return [seen[difference], i]
            else:
                seen[n] = i
        return []   



# solution 1: (bruteforce)
# take target = 7
# 7 - nums[i] = 4 (check now where 4 exists)
# if found i know the value
# if not 7 - nums[i+1] and repeat

# solution 2: using hashmap
# hashmap = {} = {(value, index)}
# seen = {}
# for i in range(len(nums)):
#     check if i+1 will make target
#         return true
#     else
#         hashmap[i] = i
#         seen = comparision done or not
# then if the seen is already done, skip and check next value
# recursion