#using heap
from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        counter = Counter(nums)           # {number: frequency}
        
        # Step 2: We will keep only k most frequent elements
        # We use min-heap → smallest frequency on top
        heap = []
        
        for num, freq in counter.items():
            if len(heap) < k:
                # Just fill first k elements
                heapq.heappush(heap, (freq, num))          # tuple: (frequency, number)
            else:
                # If current freq > smallest in heap → replace it
                heapq.heappushpop(heap, (freq, num))
                # heappushpop = push new + pop smallest in one operation
        
        # Step 3: Extract only the numbers (ignore frequencies)
        # heap contains k tuples: [(freq1,num1), (freq2,num2), ...]
        return [num for freq, num in heap]
        
## Using bucket sort
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]

#         for num in nums:
#             count[num] = 1 + count.get(num, 0)
#         for num, cnt in count.items():
#             freq[cnt].append(num)

#         res = []
#         for i in range(len(freq) - 1, 0, -1):
#             for num in freq[i]:
#                 res.append(num)
#                 if len(res) == k:
#                     return res
        