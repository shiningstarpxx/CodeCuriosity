import heapq

class MyObject:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):  # 用于最小堆的比较
        return self.value > other.value  # 反转比较逻辑，实现最大堆

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)


data = [MyObject(1), MyObject(3), MyObject(2), MyObject(4), MyObject(5)]

heapq.heapify(data)  # 建立最大堆

print("最大堆元素：")
for item in data:
    print(item)

largest = heapq.heappop(data)  # 获取最大值
print(f"最大值: {largest}")

#或者使用nlargest
largest_items = heapq.nlargest(3, data, key=lambda x: x.value)
print(f"最大的三个元素: {largest_items}")
