class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


# from typing import List

# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         result = []                     # Stores all valid combinations
        
#         def dfs(start_index: int, current_comb: List[int], current_sum: int):
#             # Base case 1: found a valid combination
#             if current_sum == target:
#                 result.append(current_comb.copy())  # copy is IMPORTANT!
#                 return
            
#             # Base case 2: invalid path
#             if current_sum > target or start_index >= len(candidates):
#                 return
            
#             # Decision 1: Include current number (and allow reuse)
#             current_comb.append(candidates[start_index])
#             # We pass start_index again → unlimited usage of same number
#             dfs(start_index, current_comb, current_sum + candidates[start_index])
            
#             # Backtrack: remove the number we just added
#             current_comb.pop()
            
#             # Decision 2: Skip current number → move to next different number
#             dfs(start_index + 1, current_comb, current_sum)
        
#         # Start recursion with empty combination and sum = 0
#         dfs(0, [], 0)
#         return result