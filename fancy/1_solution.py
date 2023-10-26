import random
import torch

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
