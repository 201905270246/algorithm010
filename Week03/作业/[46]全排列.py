# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
# import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # method 1
        # return list(itertools.permutations(nums))

        # method 2
        # res = []
        #
        # def backtrace(nums, temp):
        #     if not nums:
        #         res.append(temp)
        #         return
        #     for i in range(len(nums)):
        #         backtrace(nums[:i] + nums[i+1:], temp + [nums[i]])
        # backtrace(nums, [])
        # return res

        # method 3
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:])
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth+1, path, used, res)
                    used[i] = False
                    path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []
        used = [False for _ in range(size)]
        res = []
        dfs(nums, size, 0, [], used, res)
        return res
# leetcode submit region end(Prohibit modification and deletion)


# test locally
print(Solution().permute([1, 2, 3]))