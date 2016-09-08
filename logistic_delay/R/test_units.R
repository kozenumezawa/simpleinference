inputdata <- read.csv("../csv/input_logistic_data_connect.csv", header=FALSE)
TIMESTEP <- length(inputdata[1,])    # 
DATA_NUM <- length(inputdata[,1])    # the number of time series data


W <- read.csv("../csv/result_W_logistic.csv", header=FALSE)
b <- read.csv("../csv/result_b1_logistic.csv", header=FALSE)
UNITS_NUM <- length(W[1,])

# transpose all matrix because translate from (xW+b) to (Wx+b)
t_inputdata <- t(inputdata)
t_W <- t(W)
t_b <- t(b)

# comparison the output, visualize each output of neurons
input_1 <- read.csv("../csv/inputdata_b_0_1.csv", header=FALSE)
input_5 <- read.csv("../csv/inputdata_b_0_5.csv", header=FALSE)
input_9 <- read.csv("../csv/inputdata_b_0_9.csv", header=FALSE)
unit_outputs_1 <- t_W %*% t(input_1) + t_b[1,]
unit_outputs_5 <- t_W %*% t(input_5) + t_b[1,]
unit_outputs_9 <- t_W %*% t(input_9) + t_b[1,]

units <- 1:UNITS_NUM
plot(units, unit_outputs_1, type = "l", ylim=c(0,1), xlab = "unit number", ylab = "value", col = 'red')
par(new = TRUE)   #  Overwrite
plot(units, unit_outputs_5, type = 'l', ylim=c(0,1), xlab = '', ylab = '', col = 'blue') 
par(new = TRUE)   #  Overwrite
plot(units, unit_outputs_9, type = 'l', ylim=c(0,1), xlab = '', ylab = '', col = 'green') 


# visualize each input
t <- 1:TIMESTEP
plot(t, input_1, type = "l", ylim=c(0,1), xlab = "Time step", ylab = "value", col = 'red')
par(new = TRUE)   #  Overwrite
plot(t, input_5, type = "l", ylim=c(0,1), xlab = "Time step", ylab = "value", col = 'blue')
par(new = TRUE)   #  Overwrite
plot(t, input_9, type = "l", ylim=c(0,1), xlab = "Time step", ylab = "value", col = 'green')

# visualize each input and output
b2 <- read.csv("../csv/result_b2_logistic.csv", header=FALSE)
# b = 0.1
plot(t, input_1, type = "l", ylim=c(0,1), xlab = "Time step", ylab = "value", col = 'red')
activate_outputs <- unit_outputs_1 / (1 + abs(unit_outputs_1))
y <- data.matrix(W) %*% activate_outputs + b2
par(new = TRUE)   #  Overwrite
plot(t, t(y), type = 'l', ylim=c(0,1), xlab = '', ylab = '', col = 'black') 

# b = 0.5
plot(t, input_5, type = "l", ylim=c(0,1), xlab = "Time step", ylab = "value", col = 'red')
activate_outputs <- unit_outputs_5 / (1 + abs(unit_outputs_5))
y <- data.matrix(W) %*% activate_outputs + b2
par(new = TRUE)   #  Overwrite
plot(t, t(y), type = 'l', ylim=c(0,1), xlab = '', ylab = '', col = 'black') 

# b = 0.8
plot(t, input_9, type = "l", ylim=c(0,1), xlab = "Time step", ylab = "value", col = 'red')
activate_outputs <- unit_outputs_9 / (1 + abs(unit_outputs_9))
y <- data.matrix(W) %*% activate_outputs + b2
par(new = TRUE)   #  Overwrite
plot(t, t(y), type = 'l', ylim=c(0,1), xlab = '', ylab = '', col = 'black') 

