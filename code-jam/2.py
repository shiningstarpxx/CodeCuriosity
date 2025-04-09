def solve(H, W, altitude_map):
    # 定义方向：北、西、东、南
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    
    # 确定每个单元格的水流向
    flow = {}  # (r, c) -> (next_r, next_c) 或 None（如果是汇点）
    
    for r in range(H):
        for c in range(W):
            current_height = altitude_map[r][c]
            min_height = current_height
            flow_dir = None
            
            # 检查四个方向
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and altitude_map[nr][nc] < min_height:
                    min_height = altitude_map[nr][nc]
                    flow_dir = (nr, nc)
            
            flow[(r, c)] = flow_dir
    
    def find_sink(r, c):
        if flow[(r, c)] is None:
            return (r, c)
        next_r, next_c = flow[(r, c)]
        return find_sink(next_r, next_c)
    
    # 为每个单元格确定其排水盆地
    cell_to_sink = {}  # 将每个单元格映射到其汇点
    basin_to_cells = {}  # 将每个汇点映射到其盆地中的所有单元格
    
    for r in range(H):
        for c in range(W):
            sink = find_sink(r, c)
            cell_to_sink[(r, c)] = sink
            if sink not in basin_to_cells:
                basin_to_cells[sink] = []
            basin_to_cells[sink].append((r, c))
    
    # 找到每个盆地最先出现的单元格（按行优先顺序）
    basin_first_cells = {}
    for sink, cells in basin_to_cells.items():
        basin_first_cells[sink] = min(cells)  # 取坐标最小的单元格
    
    # 按照盆地首次出现的位置排序汇点
    sorted_sinks = sorted(basin_to_cells.keys(), key=lambda sink: basin_first_cells[sink])
    
    # 为每个汇点分配标签
    sink_labels = {}
    for i, sink in enumerate(sorted_sinks):
        sink_labels[sink] = chr(ord('a') + i)
    
    # 创建结果地图
    basin_map = [['' for _ in range(W)] for _ in range(H)]
    for r in range(H):
        for c in range(W):
            sink = cell_to_sink[(r, c)]
            basin_map[r][c] = sink_labels[sink]
    
    return basin_map

def main():
    T = int(input())
    for t in range(1, T+1):
        H, W = map(int, input().split())
        altitude_map = []
        for _ in range(H):
            altitude_map.append(list(map(int, input().split())))
        
        basin_map = solve(H, W, altitude_map)
        
        print(f"Case #{t}:")
        for row in basin_map:
            print(''.join(row))

if __name__ == '__main__':
    main()