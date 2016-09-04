data <- read.csv("../csv/result_to_compare_switch.csv", header=FALSE)

input_x <- data[1,]
input_y <- data[2,]
output_x <- data[3,]
output_y <- data[4,]

TIMESTEP <- length(data[1,])    # the length of X or Y 

t <- 1:TIMESTEP

plot(t, input_x, type = "l", ylim=c(0,1), xlab = "Time step", ylab = "value", col = 'red')
par(new = TRUE)   #  Overwrite
plot(t, output_x, type = 'l', ylim=c(0,1), xlab = '', ylab = '', col = 'blue') 

plot(t, input_y, type = "l", ylim=c(0,1), xlab = "Time step", ylab = "value", col = 'red')
par(new = TRUE)   #  Overwrite
plot(t, output_y, type = 'l', ylim=c(0,1) , xlab = '', ylab = '', col = 'blue') 

