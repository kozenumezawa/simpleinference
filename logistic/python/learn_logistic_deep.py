# coding: utf-8

import numpy
import csv
import tensorflow as tf

def weight_variable(shape, variable_name):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial, name=variable_name)


def bias_variable(shape, variable_name):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial, name=variable_name)


rawdata = numpy.load('../npy/input_logistic_data.npy')

# (10000,2,100)→(10000,200)  (to learn causality)
inputdata = numpy.zeros((rawdata.shape[0], rawdata.shape[2] * rawdata.shape[1]), dtype=numpy.float32)
for i in range(rawdata.shape[0]):
    inputdata[i,:rawdata.shape[2]] = rawdata[i, 0]       #   X
    inputdata[i, rawdata.shape[2]:] = rawdata[i, 1]      #   Y
print(inputdata.shape)

BATCH_SIZE = 1
TIME_STEP_2 = inputdata.shape[1]

x = tf.placeholder(tf.float32, [BATCH_SIZE, TIME_STEP_2], name='x')

# input to hidden 1
MIDDLE_UNIT1 = 40
W1 = weight_variable((TIME_STEP_2, MIDDLE_UNIT1), 'W1')
b1 = bias_variable([MIDDLE_UNIT1], 'b1')
DROP_OUT_RATE = 0.5
h1 = tf.nn.softsign(tf.matmul(x, W1) + b1)
keep_prob1 = tf.placeholder("float", name='keep_prob1')
h_drop1 = tf.nn.dropout(h1, keep_prob1)

# hidden1 to hidden2
MIDDLE_UNIT2 = 30
W2 = weight_variable((MIDDLE_UNIT1, MIDDLE_UNIT2), 'W2')
b2 = bias_variable([MIDDLE_UNIT2], 'b2')
h2 = tf.nn.softsign(tf.matmul(h_drop1, W2) + b2)

# hidden2 to hidden3
W3 = tf.transpose(W2)  # 転置
b3 = bias_variable([MIDDLE_UNIT1], 'b3')
h3 = tf.nn.softsign(tf.matmul(h2, W3) + b3)

# hidden3 to output
W4 = tf.transpose(W1)  # 転置
b4 = bias_variable([TIME_STEP_2], 'b2')
y = tf.nn.relu(tf.matmul(h3, W4) + b4)

loss = tf.nn.l2_loss(y - x) / BATCH_SIZE

tf.scalar_summary("l2_loss", loss)

train_step = tf.train.AdamOptimizer().minimize(loss)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)
summary_writer = tf.train.SummaryWriter('summary/l2_loss', graph_def=sess.graph_def)

DATA_NUM = 3000
# trainning loop
for step in range(DATA_NUM):
    sess.run(train_step,
             feed_dict={x: [inputdata[step]], keep_prob1: (1 - DROP_OUT_RATE)})
    summary_op = tf.merge_all_summaries()
    summary_str = sess.run(summary_op, feed_dict={x: [inputdata[step]], keep_prob1: 1.0})
    summary_writer.add_summary(summary_str, step)
    if step % 100 == 0:
        train_accuracy = loss.eval(session=sess, feed_dict={x: [inputdata[step]], keep_prob1: 1.0})
        print("step %d:%g" % (step, train_accuracy))

# Write input and output data to compare them in order to check accuracy
f = open('../csv/result_to_compare_logistic_deep.csv', 'w')
writer = csv.writer(f)
for step in range(DATA_NUM):
    one_input = [inputdata[step]]
    one_output = sess.run(y,feed_dict={x: one_input, keep_prob1: 1.0})     #   get output y
    writer.writerows(one_input)
    writer.writerows(one_output)
