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
