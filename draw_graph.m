M = csvread('inputdata.csv');

t = [1:100]

X1 = M(1,:)
Y1 = M(2,:)
X2 = M(3,:)
Y2 = M(4,:)
plot(t,X1,t,Y1)
