import hashlib

class MerkleTree:
    def __init__(self, data_list):
        self.data_list = data_list
        self.tree = []
        self.create_tree()

    def create_tree(self):
        data_list = [self.hash_data(data) for data in self.data_list]
        while len(data_list) > 1:
            data_list = self.create_parent_level(data_list)
        self.tree = data_list

    def create_parent_level(self, data_list):
        parent_level = []
        for i in range(0, len(data_list), 2):
            left = data_list[i]
            right = data_list[i + 1] if i + 1 < len(data_list) else left
            parent_level.append(self.hash_data(left + right))
        return parent_level

    def hash_data(self, data):
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def get_root(self):
        return self.tree[0] if self.tree else None