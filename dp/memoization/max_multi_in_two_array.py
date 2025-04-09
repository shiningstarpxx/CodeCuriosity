# 给你一个大小为 4 的整数数组 a 和一个大小 至少为 4 的整数数组 b。
#
#  你需要从数组 b 中选择四个下标 i0, i1, i2, 和 i3，并满足 i0 < i1 < i2 < i3。你的得分将是 a[0] * b[i0] +
#  a[1] * b[i1] + a[2] * b[i2] + a[3] * b[i3] 的值。
#
#  返回你能够获得的 最大 得分。
#
#
#
#  示例 1：
#
#
#  输入： a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7]
#
#
#  输出： 26
#
#  解释： 选择下标 0, 1, 2 和 5。得分为 3 * 2 + 2 * (-6) + 5 * 4 + 6 * 2 = 26。
#
#  示例 2：
#
#
#  输入： a = [-1,4,5,-2], b = [-5,-1,-3,-2,-4]
#
#
#  输出： -1
#
#  解释： 选择下标 0, 1, 3 和 4。得分为 (-1) * (-5) + 4 * (-1) + 5 * (-2) + (-2) * (-4) = -1
# 。
#
#
#
#  提示：
#
#
#  a.length == 4
#  4 <= b.length <= 10⁵
#  -10⁵ <= a[i], b[i] <= 10⁵
#
#
#  Related Topics 数组 动态规划 👍 10 👎 0
from linecache import cache


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        # return self.increse_order_dfs(a, b)
        return self.decrease_order_dfs(a, b)

    def increse_order_dfs(self, a: List[int], b: List[int]) -> int:
        @cache
        def dfs(i, j):
            if i == 4:
                return 0
            if j == len(b):
                return float('-inf')
            return max(dfs(i, j + 1), a[i] * b[j] + dfs(i + 1, j + 1))

        return dfs(0, 0)

    def decrease_order_dfs(self, a: List[int], b: List[int]) -> int:
        @cache
        def dfs(i, j):
            if i < 0:
                return 0
            if j < 0:
                return float('-inf')
            return max(dfs(i, j - 1), a[i] * b[j] + dfs(i - 1, j - 1))

        return dfs(3, len(b) - 1)
# leetcode submit region end(Prohibit modification and deletion)
