## 有趣的问题
#### Problem 1
* Q： 给定一些数据，我们需要做到随机且分组，如何优雅的写出这段代码


#### Problem 2
* Q： 给定一些指标，计算出这些平均指标；特别是，当这些指标在训练时分成了一些小批量

#### Problem 3
* We can divide the data into k different sets which are exclusive of each other. This is known as k-fold cross-validation.
* Q: how to implement it?
* Q: 如果数据有偏差时怎么办？ 

#### Problem 3
* 数据预处理能力，是每个ds或者researcher的必备能力，如何有效的清理数据？
* Q：数据清洗有下面几个诉求
1. 数字列标准化(x - mean) / variance  
2. 数字列如果有NaN值，用0值填充
3. 非数字列使用one hot技术打平
