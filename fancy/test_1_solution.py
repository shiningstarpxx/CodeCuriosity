import torch
import random

def data_iter(batch_size, features, labels):
    num_examples = len(features)  # 以及生成好的feature数据，就可以知道有多少个样本
    # 随机读取样本的索引，这里是从0到num_examples-1,即总共有多少个样本，就生成多少个索引
    indices = list(range(num_examples))
    # 这些样本是随机读取的，没有特定的顺序
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        batch_indices = torch.tensor(
            indices[i: min(i + batch_size, num_examples)])
        yield features[batch_indices], labels[batch_indices]

def test_data_iter():
    def check_data(batch_size, features, labels):
        data = list(data_iter(batch_size, features, labels))

        # Check if the number of batches is correct
        assert len(data) == (len(features) + batch_size - 1) // batch_size

        # Check if all features and labels are returned
        returned_features = torch.cat([batch[0] for batch in data])
        returned_labels = torch.cat([batch[1] for batch in data])

        assert torch.equal(torch.sort(returned_features, dim=0)[0], torch.sort(features, dim=0)[0])
        assert torch.equal(torch.sort(returned_labels, dim=0)[0], torch.sort(labels, dim=0)[0])

    # Test case 1
    batch_size = 2
    features = torch.tensor([[1, 2], [3, 4], [5, 6], [7, 8]])
    labels = torch.tensor([0, 1, 2, 3])
    check_data(batch_size, features, labels)

    # Test case 2
    batch_size = 3
    features = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    labels = torch.tensor([0, 1, 2])
    check_data(batch_size, features, labels)

    # Test case 3
    batch_size = 1
    features = torch.tensor([[1, 2], [3, 4], [5, 6], [7, 8]])
    labels = torch.tensor([0, 1, 2, 3])
    check_data(batch_size, features, labels)

    print("All test cases pass")

test_data_iter()


def test_data_iter_reasonable():
    # 创建虚拟的 features 和 labels 数据
    features = torch.randn(100, 2)
    labels = torch.randint(0, 2, (100,))

    # 设置 batch_size
    batch_size = 10

    # 调用 data_iter 函数
    batches = list(data_iter(batch_size, features, labels))

    # 检查返回的批次数量是否正确
    assert len(batches) == (len(features) + batch_size - 1) // batch_size, "Incorrect number of batches"

    # 检查每个批次的大小是否正确
    for i, (batch_features, batch_labels) in enumerate(batches):
        if i < len(batches) - 1:
            assert batch_features.shape[0] == batch_size, f"Incorrect batch size in batch {i}"
            assert batch_labels.shape[0] == batch_size, f"Incorrect batch size in batch {i}"
        else:
            # 最后一个批次可能小于 batch_size
            remaining = len(features) % batch_size
            expected_size = remaining if remaining != 0 else batch_size
            assert batch_features.shape[0] == expected_size, f"Incorrect batch size in batch {i}"
            assert batch_labels.shape[0] == expected_size, f"Incorrect batch size in batch {i}"

    # 检查所有样本是否都被返回了
    all_features = torch.cat([batch_features for batch_features, _ in batches])
    all_labels = torch.cat([batch_labels for _, batch_labels in batches])
    assert torch.equal(torch.sort(all_features, dim=0)[0], torch.sort(features, dim=0)[0]), "Not all features returned"
    assert torch.equal(torch.sort(all_labels, dim=0)[0], torch.sort(labels, dim=0)[0]), "Not all labels returned"


test_data_iter_reasonable()

print("test is over")