使用索引之后如果我们是频繁查询某一个字段，那么速度会有显著的提高。

Here are the results of running the experiment on a dataset of 1 50 thousand students:

- Time without index: 30.12371063232422 ms
- Time with index: 1.2662410736083984 ms

实验连接的是本地mysql实例。用python脚本随机添加了大概500000个数据。