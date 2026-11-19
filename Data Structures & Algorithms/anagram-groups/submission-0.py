class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorting
        # result = defaultdict(list)
        # for val in strs:
        #     sortedS = ''.join(sorted(val))
        #     result[sortedS].append(val)
        # return list(result.values())

        # using hashmap
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)
        return list(result.values())


        # if len(strs) <= 1:
        #     return [strs]
        # else:
        #     sizeHash = {}
        #     sortedHash = {}
        #     for i in range(len(strs)):
        #         sizeHash[i] = [i, get(len(strs[i]), 0)]
        #         sortedHash = sorted(sizeHash) # technically should give me sorted list
        #         for eachSort, freq in enumerate(sortedHash):
        #             while freq == sortedHash[i]


# check if list is empty or has 1 entry, if yes return the same
# take all the list elements and place them hashmaps based on char len
#     sizehash = [[act, 3], [pots, 4]]
# now i can directly take al the common sizes
# [3], [4] and so on
# for each of these lists:
#     counter[3letters] is the same
#     sorted
#     if yes, return the []
#     if not, split the list [[], []]
#     recrusion