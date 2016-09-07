data <- read.csv("../csv/result_to_compare_transient.csv", header=FALSE)

data_index <- 1  # the numbr of data which we want to

input <- data[data_index * 2 + 1,]
output <- data[data_index * 2 + 2,]

TIMESTEP <- length(data[1,])    # the length of X or Y 

t <- 1:TIMESTEP

# comparison
plot(t, input, type = "l", ylim=c(0,1), xlab = "Time step", ylab = "value", col = 'red')
par(new = TRUE)   #  Overwrite
plot(t, output, type = 'l', ylim=c(0,1), xlab = '', ylab = '', col = 'blue') 

