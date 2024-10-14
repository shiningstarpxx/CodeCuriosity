# 给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。
#
#  已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。
#
#  每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎
# ，则可以在之后的操作中 重复使用 这枚鸡蛋。
#
#  请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？
#
#  示例 1：
#
#
# 输入：k = 1, n = 2
# 输出：2
# 解释：
# 鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。
# 否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。
# 如果它没碎，那么肯定能得出 f = 2 。
# 因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。
#
#
#  示例 2：
#
#
# 输入：k = 2, n = 6
# 输出：3
#
#
#  示例 3：
#
#
# 输入：k = 3, n = 14
# 输出：4
#
#
#
#
#  提示：
#
#
#  1 <= k <= 100
#  1 <= n <= 10⁴
#
#
#  Related Topics 数学 二分查找 动态规划 👍 1020 👎 0
from functools import cache
from itertools import count


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        return self.rawDfs(k, n)
        #return self.min_moves(k, n)

    # Time complexity: O(kn), performance is the best
    def rawDfs(self, k: int, n: int) -> int:
        @cache
        def dfs(i: int, j: int) -> int:  # i是操作次数，j是鸡蛋数
            if i == 0 or j == 0:
                return 0
            return dfs(i - 1, j - 1) + dfs(i - 1, j) + 1

        for i in count(1):
            if dfs(i, k) >= n:
                return i

    # Time complexity: O(knlogn), theoretical performance is the best, but actual performance is worse
    def min_moves(self, k: int, n: int) -> int:
        @cache
        def dfs(moves: int, eggs: int) -> int:
            if moves == 0 or eggs == 0:
                return 0

            return dfs(moves - 1, eggs - 1) + dfs(moves - 1, eggs) + 1

        low, high = 1, n  # Binary search bounds
        while low <= high:
            mid = (low + high) // 2
            if dfs(mid, k) >= n:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def optimizeDfs(self, k: int, n : int) -> int:
        @cache
        def dfs(k: int, n: int) -> int:
            if k == 1:
                return n
            if n == 0:
                return 0

            left, right = 1, n
            while left < right:
                mid = (left + right) // 2
                broken = dfs(k - 1, mid - 1)
                not_broken = dfs(k, n - mid)
                if broken < not_broken:
                    left = mid + 1
                else:
                    right = mid

            return 1 + min(max(dfs(k - 1, left - 1), dfs(k, n - left)),
                           max(dfs(k - 1, right - 1), dfs(k, n - right)))

        return dfs(k, n)
# leetcode submit region end(Prohibit modification and deletion)
