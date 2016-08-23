data <- read.csv("../csv/inputdata_b_low.csv", header=FALSE)
input_x_low <- data[1,]
input_y_low <- data[2,]

data <- read.csv("../csv/inputdata_b_high.csv", header=FALSE)
input_x_high <- data[1,]
input_y_high <- data[2,]

TIMESTEP <- length(data[1,])    # the length of X or Y 
t <- 1:TIMESTEP

plot(t, input_x_low, type = "l", ylim=c(0,1), xlab = "Time step", ylab = "value", col = 'red', main="xとyのグラフ(b=0)")
par(new = TRUE)   #  Overwrite
plot(t, input_y_low, type = 'l', ylim=c(0,1), xlab = '', ylab = '', col = 'blue') 

plot(t, input_x_high, type = "l", ylim=c(0,1), xlab = "Time step", ylab = "value", col = 'red', main="xとyのグラフ(b=0.95)")
par(new = TRUE)   #  Overwrite
plot(t, input_y_high, type = 'l', ylim=c(0,1), xlab = '', ylab = '', col = 'blue') 

plot(t, input_x_low, type = "l", ylim=c(0,1), xlab = "Time step", ylab = "value", col = 'red', main="xのグラフ(b=0, b=0.95)")
par(new = TRUE)   #  Overwrite
plot(t, input_x_high, type = 'l', ylim=c(0,1), xlab = '', ylab = '', col = 'blue') 

plot(t, input_y_low, type = "l", ylim=c(0,1), xlab = "Time step", ylab = "value", col = 'red', main="yのグラフ(b=0, b=0.95)")
par(new = TRUE)   #  Overwrite
plot(t, input_y_high, type = 'l', ylim=c(0,1), xlab = '', ylab = '', col = 'blue') 

