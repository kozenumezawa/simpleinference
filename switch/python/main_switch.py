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


inputdata = numpy.load('../npy/input_switch_data.npy')

DATA_PAIR = inputdata.shape[1]
TIME_STEP_2 = inputdata.shape[2]

x = tf.placeholder(tf.float32, [DATA_PAIR, TIME_STEP_2], name='x')

MIDDLE_UNIT = 25
W = weight_variable((TIME_STEP_2, MIDDLE_UNIT), 'W')
b1 = bias_variable([MIDDLE_UNIT], 'b1')

DROP_OUT_RATE = 0.5

h = tf.nn.softsign(tf.matmul(x, W) + b1)
keep_prob = tf.placeholder("float", name='keep_prob')
h_drop = tf.nn.dropout(h, keep_prob)

W2 = tf.transpose(W)  # 転置
b2 = bias_variable([TIME_STEP_2], 'b2')
y = tf.nn.relu(tf.matmul(h_drop, W2) + b2)

loss = tf.nn.l2_loss(y - x) / DATA_PAIR

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
             feed_dict={x: inputdata[step], keep_prob: (1 - DROP_OUT_RATE)})
    summary_op = tf.merge_all_summaries()
    summary_str = sess.run(summary_op, feed_dict={x: inputdata[step], keep_prob: 1.0})
    summary_writer.add_summary(summary_str, step)
    if step % 100 == 0:
        train_accuracy = loss.eval(session=sess, feed_dict={x: inputdata[step], keep_prob: 1.0})
        print("step %d:%g" % (step, train_accuracy))

# Write input and output data to compare them in order to check accuracy
f = open('../csv/result_to_compare_switch.csv', 'w')
writer = csv.writer(f)
for step in range(DATA_NUM):
    one_input = inputdata[step]
    one_output = sess.run(y,feed_dict={x: one_input, keep_prob: 1.0})     #   get output y
    writer.writerows(one_input)
    writer.writerows(one_output)

# Write weights W
result = sess.run(W2)
numpy.save('../npy/result_W_switch.npy', result)
f = open('../csv/result_W_switch.csv', 'w')
writer = csv.writer(f)
for step in range(MIDDLE_UNIT):
    result_w = result[step].tolist()
    writer.writerows([result_w])
