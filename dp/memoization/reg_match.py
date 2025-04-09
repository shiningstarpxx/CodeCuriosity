# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
#
#  '.' 匹配任意单个字符
#  '*' 匹配零个或多个前面的那一个元素
#
#
#  所谓匹配，是要涵盖 整个 字符串 s 的，而不是部分字符串。
#
#  示例 1：
#
#
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
#
#
#  示例 2:
#
#
# 输入：s = "aa", p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#
#
#  示例 3：
#
#
# 输入：s = "ab", p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 20
#  1 <= p.length <= 20
#  s 只包含从 a-z 的小写字母。
#  p 只包含从 a-z 的小写字母，以及字符 . 和 *。
#  保证每次出现字符 * 时，前面都匹配到有效的字符
#
#
#  Related Topics 递归 字符串 动态规划 👍 3977 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                return dfs(i, j + 2) or first_match and dfs(i + 1, j)
            else:
                return first_match and dfs(i + 1, j + 1)

        return dfs(0, 0)

    def tabulation(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j] 表示 s 的前 i 个字符与 p 的前 j 个字符是否能够匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(2, n + 1):
            dp[0][i] = dp[0][i - 2] and p[i - 1] == '*'

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    if dp[i][j - 2]:
                        dp[i][j] = True
                    elif dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'):
                        dp[i][j] = True
                else:
                    if dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.'):
                        dp[i][j] = True

        return dp[m][n]
# leetcode submit region end(Prohibit modification and deletion)
