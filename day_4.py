import tensorflow as tf
c1=tf.constant(9.5,dtype=tf.float32)
a=tf.Variable(2.5)
b=tf.Variable(2.9)
z=tf.Variable([[ 2,3,4],[3,4,5]])
sum=tf.Variable(1)
sess=tf.Session()
sess.run(tf.global_variables_initializer())
print('变量a与常量c1的差：',sess.run(tf.subtract(a,c1)))
print('两个变量a和b的和：',sess.run(a+b))
print('两个变量a和b的乘积:',sess.run(a*b))
print('转置函数:\n',sess.run(tf.transpose(z)))

for i in range(1,11,2):

    # sum=sum*i
    print(sess.run(sum),'*',i,'=',sess.run(tf.assign(sum,tf.multiply(sum,i))))

