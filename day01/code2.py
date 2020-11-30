import tensorflow as tf

a = tf.constant([1, 2, 3], tf.int64)
print(a)
# tf.Tensor([1 2 3], shape=(3,), dtype=int64)
print(a.dtype)
# <dtype: 'int64'>
print(a.shape)
# (3,)
#####################################################################

# 创建全为0的张量
zeros = tf.zeros([2, 3], tf.int64)
print(zeros)

# 创建全为1的张量
ones = tf.ones([3, 2], tf.int64)
print(ones)

# 创建为指定值的张量
fill = tf.fill([2, 3], 7, tf.int64)
print(fill)

#####################################################################
"""
tf.data.Dataset.from_tensor_slices()为特征和标签配对的函数
"""
features = tf.constant([12, 15, 60, 70, 85])
labels = tf.constant([1, 1, 0, 0, 0])
dataset = tf.data.Dataset.from_tensor_slices((features, labels))
print(dataset)
for element in dataset:
    print(element)
"""
<TensorSliceDataset shapes: ((), ()), types: (tf.int32, tf.int32)>
(<tf.Tensor: id=19, shape=(), dtype=int32, numpy=12>, <tf.Tensor: id=20, shape=(), dtype=int32, numpy=1>)
(<tf.Tensor: id=21, shape=(), dtype=int32, numpy=15>, <tf.Tensor: id=22, shape=(), dtype=int32, numpy=1>)
(<tf.Tensor: id=23, shape=(), dtype=int32, numpy=60>, <tf.Tensor: id=24, shape=(), dtype=int32, numpy=0>)
(<tf.Tensor: id=25, shape=(), dtype=int32, numpy=70>, <tf.Tensor: id=26, shape=(), dtype=int32, numpy=0>)
(<tf.Tensor: id=27, shape=(), dtype=int32, numpy=85>, <tf.Tensor: id=28, shape=(), dtype=int32, numpy=0>)
"""
