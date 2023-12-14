import hashlib
import unittest

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



class TestMerkleTree(unittest.TestCase):
    def test_create_tree(self):
        data_list = ["a", "b", "c", "d"]
        mt = MerkleTree(data_list)
        self.assertIsNotNone(mt.tree)

    def test_get_root(self):
        data_list1 = ["a", "b", "c", "d"]
        mt1 = MerkleTree(data_list1)
        data_list2 = ["a", "b", "c", "e"]
        mt2 = MerkleTree(data_list2)

        self.assertNotEqual(mt1.get_root(), mt2.get_root())

        data_list3 = ["a", "b", "c", "d"]
        mt3 = MerkleTree(data_list3)

        self.assertEqual(mt1.get_root(), mt3.get_root())