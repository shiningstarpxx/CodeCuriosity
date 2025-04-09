# 给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。你可以将球移到在四个方向上相邻的单元格内（可以
# 穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。
#
#  给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对
# 10⁹ + 7 取余 后的结果。
#
#
#
#  示例 1：
#
#
# 输入：m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# 输出：6
#
#
#  示例 2：
#
#
# 输入：m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# 输出：12
#
#
#
#
#  提示：
#
#
#  1 <= m, n <= 50
#  0 <= maxMove <= 50
#  0 <= startRow < m
#  0 <= startColumn < n
#
#
#  Related Topics 动态规划 👍 317 👎 0
from linecache import cache


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(x: int, y: int, k: int) -> int:
            if x < 0 or x >= m or y < 0 or y >= n:
                return 1
            if k == 0:
                return 0

            count = 0
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                count = (count + dfs(x + dx, y + dy, k - 1) % MOD) % MOD
            return count

        return dfs(startRow, startColumn, maxMove)

# leetcode submit region end(Prohibit modification and deletion)
