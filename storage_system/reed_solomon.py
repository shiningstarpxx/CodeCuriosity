from reedsolo import RSCodec

# 初始化 Reed-Solomon 编码器，n=10, k=4 表示将 10 个数据块编码成 14 个块 (包括 4 个校验块)
rs = RSCodec(4)

# 原始数据
data = b'This is some sample data to encode.'

# 编码数据
encoded_data = rs.encode(data)

# 模拟数据块丢失 (例如丢失第 3 和第 7 个块)
encoded_data[2] = 255
encoded_data[6] = 255

# 模拟数据块损坏 (例如损坏第 2 和第 6 个块)
# del encoded_data[6]
# del encoded_data[2]
# reedsolo.ReedSolomonError: Too many (or few) errors found by Chien Search for the errata locator polynomial!

# 解码数据
decoded_data = rs.decode(encoded_data)[0]

# 输出解码后的数据
print(decoded_data)  # 输出: b'This is some sample data to encode.'