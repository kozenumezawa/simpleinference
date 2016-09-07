inputdata <- read.csv("../csv/input_transient_data_connect.csv", header=FALSE)
TIMESTEP <- length(inputdata[1,])    # 
DATA_NUM <- length(inputdata[,1])    # the number of time series data


W <- read.csv("../csv/result_W_transient.csv", header=FALSE)
b <- read.csv("../csv/result_b_transient.csv", header=FALSE)

UNITS_NUM <- length(W[1,])
# transpose all matrix because translate from (xW+b) to (Wx+b)
t_inputdata <- t(inputdata)
t_W <- t(W)
t_b <- t(b)

units <- 1:UNITS_NUM

data_index <- 3
# comparison
unit_outputs <- t_W %*% t_inputdata[,data_index] + t_b[1,]
plot(units, unit_outputs, type = "l", ylim=c(0,1), xlab = "Time step", ylab = "value", col = 'red')
par(new = TRUE)   #  Overwrite
plot(t, output, type = 'l', ylim=c(0,1), xlab = '', ylab = '', col = 'blue') 
