# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 
# 
#  示例: 
# 
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
#  Related Topics 回溯算法

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k <= 0 or n <= 0 or k > n:
            return []
        res = []
        self.__dfs(1, k, n, [], res)
        return res

    def __dfs(self, start, k, n, pre, res):
        if len(pre) == k:
            res.append(pre[:])
            return
        for i in range(start, n - (k - len(pre)) + 2):
            pre.append(i)
            self.__dfs(i+1, k, n, pre, res)
            pre.pop()

# leetcode submit region end(Prohibit modification and deletion)


# test locally
print(Solution().combine(4, 2))
