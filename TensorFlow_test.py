# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 08:40:01 2018

@author: 014277960
"""

import tensorflow as tf

a = tf.constant([1.0,2.0],name="a")
b = tf.constant([2.0,3.0],name="b")

result = a+b
print(a.graph is tf.get_default_graph())
sess = tf.Session()
print(sess.run(result))


































