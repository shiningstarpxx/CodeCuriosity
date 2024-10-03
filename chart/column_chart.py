import matplotlib.pyplot as plt
import numpy as np

# 示例数据 (替换为你的实际数据)
sizes = ["0-50MB", "50-100MB", "100-150MB", "150-200MB", "200-250MB", "250-300MB", "大于300MB"]
new_created = [4700000, 300000, 100000, 10000, 10000, 10000, 10000]
in_use_material = [200000, 100000, 10000, 10000, 10000, 10000, 10000]
in_use_creative = [500000, 300000, 100000, 10000, 10000, 10000, 10000]

x = np.arange(len(sizes))
width = 0.25

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, new_created, width, label='新创建素材个数')
rects2 = ax.bar(x, in_use_material, width, label='在投素材个数')
rects3 = ax.bar(x + width, in_use_creative, width, label='在投创意个数')

ax.set_yscale('symlog') # 设置y轴为对数刻度
ax.set_xticks(x)
ax.set_xticklabels(sizes)
ax.legend()

fig.tight_layout()
plt.show()