class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]


        # [3,4,5,6,1,2]

        # 0 + 5 // 2 = 3
        # 0 + (5-0) 

        # l=0
        # r=5
        # [4,5,6,1,2,3]
        # m=3
        # 1 < 3
        # r=3
        # l=0

        # m=2
        # so, l=3,r=3

