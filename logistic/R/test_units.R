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

# create testdata which do not have causal relation
testdata <- array(data = 0, dim = c(TIMESTEP))
for (i in 1:TIMESTEP) {
  testdata[i] <- runif(1)
  i <- i + 1
}

# comparison
data_index <- 20
unit_outputs_1 <- t_W %*% t_inputdata[,data_index] + t_b[1,]
unit_outputs_2 <- t_W %*% testdata + t_b[1,]

units <- 1:UNITS_NUM
plot(units, unit_outputs_1, type = "l", ylim=c(0,1), xlab = "Time step", ylab = "value", col = 'red')
par(new = TRUE)   #  Overwrite
plot(units, unit_outputs_2, type = 'l', ylim=c(0,1), xlab = '', ylab = '', col = 'blue') 
# plot(units, t_b[1,], type = 'l', ylim=c(0,1), xlab = '', ylab = '', col = 'blue') 

# visualize each input
t <- 1:TIMESTEP
plot(t, t_inputdata[,data_index], type = "l", ylim=c(0,1), xlab = "Time step", ylab = "value", col = 'red')
par(new = TRUE)   #  Overwrite
plot(t, testdata, type = 'l', ylim=c(0,1), xlab = '', ylab = '', col = 'blue') 

# visualize autoencoder output
activate_outputs <- unit_outputs_1 / (1 + abs(unit_outputs_1))
b2 <- read.csv("../csv/result_b2_logistic.csv", header=FALSE)
y <- data.matrix(W) %*% activate_outputs + b2
par(new = TRUE)   #  Overwrite
plot(t, t(y), type = 'l', ylim=c(0,1), xlab = '', ylab = '', col = 'green') 

