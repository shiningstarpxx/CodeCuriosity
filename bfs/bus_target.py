# 给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。
#
#
#  例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1
# -> ... 这样的车站路线行驶。
#
#
#  现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。
#
#  求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。
#
#
#
#  示例 1：
#
#
# 输入：routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# 输出：2
# 解释：最优策略是先乘坐第一辆公交车到达车站 7 , 然后换乘第二辆公交车到车站 6 。
#
#
#  示例 2：
#
#
# 输入：routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# 输出：-1
#
#
#
#
#  提示：
#
#
#  1 <= routes.length <= 500.
#  1 <= routes[i].length <= 10⁵
#  routes[i] 中的所有值 互不相同
#  sum(routes[i].length) <= 10⁵
#  0 <= routes[i][j] < 10⁶
#  0 <= source, target < 10⁶
#
#
#  Related Topics 广度优先搜索 数组 哈希表 👍 391 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target:
            return 0

        # 记录每个车站可以乘坐的公交车
        station_to_bus = {}
        for i, route in enumerate(routes):
            for station in route:
                if station not in station_to_bus:
                    station_to_bus[station] = []
                station_to_bus[station].append(i)

        # 记录每辆公交车可以到达的车站
        # bus_to_station = [set(route) for route in routes]

        # BFS
        visited_bus = set()
        visited_station = set()
        queue = [(source, 0)]
        while queue:
            station, step = queue.pop(0)
            for bus in station_to_bus.get(station, []):
                if bus in visited_bus:
                    continue
                visited_bus.add(bus)
                for next_station in routes[bus]:
                    if next_station in visited_station:
                        continue
                    visited_station.add(next_station)
                    if next_station == target:
                        return step + 1
                    queue.append((next_station, step + 1))
        return -1
# leetcode submit region end(Prohibit modification and deletion)
