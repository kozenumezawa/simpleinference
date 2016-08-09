
inputdata <- read.csv("./csv/result_w.csv", header=FALSE)
N_DATA <- length(inputdata[,1])      #the number of units
TIMESTEP <- length(inputdata[1,])    # the length of X or Y 

t <- 1:TIMESTEP

# show  inputdata
W <- array(data = 0, dim = c(N_DATA, TIMESTEP))
W <- inputdata
index <- 1
#for (i in 1:N_DATA) {
  plot(t, W[50,], type = "l", xlab = "Time step", ylab = "value")
 # i <- i + 1
#}

