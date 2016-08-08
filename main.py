# coding: utf-8

import numpy

import tensorflow as tf


def weight_variable(shape, variable_name):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial, name=variable_name)


def bias_variable(shape, variable_name):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial, name=variable_name)


def main():
    rawdata = numpy.load('ocean.normalized.npy')
    data = numpy.zeros((rawdata.shape[0] * 6, rawdata.shape[2] * 2),
                       dtype=numpy.float32)
    for i in range(rawdata.shape[0]):
        data[i * 6, :rawdata.shape[2]] = rawdata[i, 0]      #   S(salinity)
        data[i * 6, rawdata.shape[2]:] = rawdata[i, 1]      #   T(water temperature)
        data[i * 6 + 1, :rawdata.shape[2]] = rawdata[i, 0]  #   S(salinity)
        data[i * 6 + 1, rawdata.shape[2]:] = rawdata[i, 2]  #   V(flow velocity)
        data[i * 6 + 2, :rawdata.shape[2]] = rawdata[i, 1]  #   T(water temperature)
        data[i * 6 + 2, rawdata.shape[2]:] = rawdata[i, 0]  #   S(salinity)
        data[i * 6 + 3, :rawdata.shape[2]] = rawdata[i, 1]  #   T(water temperature)
        data[i * 6 + 3, rawdata.shape[2]:] = rawdata[i, 2]  #   V(flow velocity)
        data[i * 6 + 4, :rawdata.shape[2]] = rawdata[i, 2]  #   V(flow velocity)
        data[i * 6 + 4, rawdata.shape[2]:] = rawdata[i, 0]  #   S(salinity)
        data[i * 6 + 5, :rawdata.shape[2]] = rawdata[i, 2]  #   V(flow velocity)
        data[i * 6 + 5, rawdata.shape[2]:] = rawdata[i, 1]  #   T(water temperature)
    print(data.shape)


    PIXELS = data.shape[1]
    H = 25
    BATCH_SIZE = data.shape[0]
    DROP_OUT_RATE = 0.5

    x = tf.placeholder(tf.float32, [BATCH_SIZE, PIXELS], name='x')

    W = weight_variable((PIXELS, H), 'W')
    b1 = bias_variable([H], 'b1')

    h = tf.nn.softsign(tf.matmul(x, W) + b1)
    keep_prob = tf.placeholder("float", name='keep_prob')
    h_drop = tf.nn.dropout(h, keep_prob)

    W2 = tf.transpose(W)  # 転置
    b2 = bias_variable([PIXELS], 'b2')
    y = tf.nn.relu(tf.matmul(h_drop, W2) + b2)

    loss = tf.nn.l2_loss(y - x) / BATCH_SIZE

    tf.scalar_summary("l2_loss", loss)

    train_step = tf.train.AdamOptimizer().minimize(loss)

    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)
    summary_writer = tf.train.SummaryWriter('summary/l2_loss',
                                            graph=sess.graph)

    for step in range(2001):
        sess.run(train_step,
                 feed_dict={x: data, keep_prob: (1 - DROP_OUT_RATE)})
        summary_op = tf.merge_all_summaries()
        summary_str = sess.run(summary_op,
                               feed_dict={x: data, keep_prob: 1.0})
        summary_writer.add_summary(summary_str, step)
        if step % 100 == 0:
            print(loss.eval(session=sess,
                            feed_dict={x: data, keep_prob: 1.0}))

    result = sess.run(W2)
    print(result)
    numpy.save('result.npy', result)

    # Draw Encode/Decode Result
    # plt.figure(figsize=(N_COL, N_ROW * 2.5))
    # for row in range(N_ROW):
    #     for col in range(N_COL):
    #         i = row * N_COL + col
    #         d = result[i]
    #         plt.subplot(2 * N_ROW, N_COL, 2 * row * N_COL + col + 1)
    #         plt.title('W:{:02}'.format(i))
    #         plt.imshow(d.reshape((8, PIXELS // 8)),
    #                    cmap="magma",
    #                    clim=(-1.0, 1.0),
    #                    origin='upper')
    #         plt.tick_params(labelbottom="off")
    #         plt.tick_params(labelleft="off")
    # plt.savefig("result.png")
    # plt.show()

if __name__ == '__main__':
    main()
