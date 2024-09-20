# 如果一个正整数每一个数位都是 互不相同 的，我们称它是 特殊整数 。
#
#  给你一个 正 整数 n ，请你返回区间 [1, n] 之间特殊整数的数目。
#
#
#
#  示例 1：
#
#
# 输入：n = 20
# 输出：19
# 解释：1 到 20 之间所有整数除了 11 以外都是特殊整数。所以总共有 19 个特殊整数。
#
#
#  示例 2：
#
#
# 输入：n = 5
# 输出：5
# 解释：1 到 5 所有整数都是特殊整数。
#
#
#  示例 3：
#
#
# 输入：n = 135
# 输出：110
# 解释：从 1 到 135 总共有 110 个整数是特殊整数。
# 不特殊的部分数字为：22 ，114 和 131 。
#
#
#
#  提示：
#
#
#  1 <= n <= 2 * 10⁹
#
#
#  Related Topics 数学 动态规划 👍 102 👎 0
class Solution:
    def countSpecialNumbers(self, n: int):

        @cache
        def dp(mask: int, prefixSmaller: bool):
            if mask.bit_count() == len(nStr):
                return 1
            res = 0
            lowerBound = 1 if mask == 0 else 0
            upperBound = 9 if prefixSmaller else int(nStr[mask.bit_count()])
            for i in range(lowerBound, upperBound + 1):
                if mask >> i & 1 == 0:
                    res += dp(mask | 1 << i, prefixSmaller or i < upperBound)
            return res

        nStr = str(n)
        res = 0
        prod = 9
        for i in range(len(nStr) - 1):
            res += prod
            prod *= 9 - i
        res += dp(0, False)
        dp.cache_clear()
        return res