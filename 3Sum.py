class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        ret = set()
        arr = sorted(nums)

        for i in range(l - 2):
            j = i + 1
            k = l - 1

            while j < k:
                total = arr[i] + arr[j] + arr[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    if (arr[i], arr[j], arr[k]) not in ret:
                        ret.add((arr[i], arr[j], arr[k]))
                    j += 1
                    k -= 1

        return list(ret)
