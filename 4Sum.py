class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l = len(nums)
        arr = sorted(nums)
        ret = set()

        for i in range(l - 3):
            for j in range(i + 1, l - 2):
                a = j + 1
                b = l - 1

                while a < b:
                    total = arr[i] + arr[j] + arr[a] + arr[b]

                    if total < target:
                        a += 1
                    elif total > target:
                        b -= 1
                    else:
                        if (arr[i], arr[j], arr[a], arr[b]) not in ret:
                            ret.add((arr[i], arr[j], arr[a], arr[b]))

                        a += 1
                        b -= 1

        return list(ret)
