import random

class Node:
    def __init__(self, key, value, level):
        self.key = key
        self.value = value
        self.next = [None] * level

class SkipList:
    def __init__(self, max_level=16, p=0.25):
        self.max_level = max_level
        self.p = p
        self.head = Node(None, None, max_level)
        self.level = 1

    def random_level(self):
        level = 1
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def insert(self, key, value):
        update = [None] * self.max_level
        current = self.head

        for i in range(self.level - 1, -1, -1):
            while current.next[i] and current.next[i].key < key:
                current = current.next[i]
            update[i] = current

        current = current.next[0]

        if current and current.key == key:
            current.value = value
        else:
            new_level = self.random_level()
            if new_level > self.level: # 这个部分的代码是最tricky的
                for i in range(self.level, new_level):
                    update[i] = self.head
                self.level = new_level

            new_node = Node(key, value, new_level)
            for i in range(new_level):
                new_node.next[i] = update[i].next[i]
                update[i].next[i] = new_node

    def search(self, key):
        current = self.head
        for i in range(self.level - 1, -1, -1):
            while current.next[i] and current.next[i].key < key:
                current = current.next[i]

        current = current.next[0]
        if current and current.key == key:
            return current.value
        else:
            return None


# 示例用法
skiplist = SkipList()
skiplist.insert("apple", 1)
skiplist.insert("banana", 2)
skiplist.insert("orange", 3)

print(skiplist.search("banana"))  # 输出 2
print(skiplist.search("grape"))   # 输出 None