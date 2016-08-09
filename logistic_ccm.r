library(multispatialCCM)
library(rEDM)

inputdata <- read.csv("inputdata.csv", header=FALSE)
N_DATA <- length(inputdata[,1]) / 2  # the number of X or Y
TIMESTEP <- length(inputdata[1,])    # the length of X or Y 

t <- 1:TIMESTEP

# show  inputdata
X <- array(data = 0, dim = c(N_DATA, TIMESTEP))
Y <- array(data = 0, dim = c(N_DATA, TIMESTEP))
index <- 1
for (i in 1:N_DATA) {
  for(j in 1:TIMESTEP) {
    X[i,j] <- inputdata[index,j]
    Y[i,j] <- inputdata[index+1,j] 
    j <- j + 1
  }
  index <- index + 2
  i <- i + 1
}
plot(t, X[2,], type = "l", xlab = "Time step", ylab = "value")
plot(t, Y[2,], type = "l", xlab = "Time step", ylab = "value")


Accm <- X[1,]
Bccm <- Y[1,]

# determine Embedding Dimension
lib <- c(1, 20)
pred <- c(40, 80)
simplex_output <- simplex(Accm, lib, pred)
par(mar = c(4, 4, 1, 1), mgp = c(2.5, 1, 0))
plot(simplex_output$E, simplex_output$rho, type = "l", xlab = "Embedding Dimension (E)", ylab = "Forecast Skill (rho)")

simplex_output <- simplex(Bccm, lib, pred)
par(mar = c(4, 4, 1, 1), mgp = c(2.5, 1, 0))
plot(simplex_output$E, simplex_output$rho, type = "l", xlab = "Embedding Dimension (E)", ylab = "Forecast Skill (rho)")

# Prediction Decay
simplex_output <- simplex(Accm, lib, pred, E = 4, tp = 1:10)
par(mar = c(4, 4, 1, 1))
plot(simplex_output$tp, simplex_output$rho, type = "l", xlab = "Time to Prediction (tp)", ylab = "Forecast Skill (rho)")

simplex_output <- simplex(Bccm, lib, pred, E = 4, tp = 1:10)
par(mar = c(4, 4, 1, 1))
plot(simplex_output$tp, simplex_output$rho, type = "l", xlab = "Time to Prediction (tp)", ylab = "Forecast Skill (rho)")

# Identifying Nonlinearity
smap_output <- s_map(Accm, lib, pred, E=4)
par(mar = c(4, 4, 1, 1), mgp = c(2.5, 1, 0))
plot(smap_output$theta, smap_output$rho, type = "l", xlab = "Nonlinearity (theta)", ylab = "Forecast Skill (rho)")

smap_output <- s_map(Bccm, lib, pred, E=4)
par(mar = c(4, 4, 1, 1), mgp = c(2.5, 1, 0))
plot(smap_output$theta, smap_output$rho, type = "l", xlab = "Nonlinearity (theta)", ylab = "Forecast Skill (rho)")

# CCM(use multispatialCCM)
E_A <- 4
E_B <- 4
signal_A_out<-SSR_check_signal(A=Accm, E=E_A, tau=2, predsteplist=1:10)
signal_B_out<-SSR_check_signal(A=Bccm, E=E_B, tau=2, predsteplist=1:10)
CCM_boot_A<-CCM_boot(Accm, Bccm, E_A, tau=2, iterations=10)
CCM_boot_B<-CCM_boot(Bccm, Accm, E_B, tau=2, iterations=10)
(CCM_significance_test<-ccmtest(CCM_boot_A, CCM_boot_B))
plotxlimits<-range(c(CCM_boot_A$Lobs, CCM_boot_B$Lobs))
plot(CCM_boot_A$Lobs, CCM_boot_A$rho, type="l", col=1, lwd=2, xlim=c(plotxlimits[1], plotxlimits[2]), ylim=c(0,1), xlab="Library Size", ylab="Cross Map Skill (rho)", cex.lab = 1.5)
lines(CCM_boot_B$Lobs, CCM_boot_B$rho, type="l", col=2, lty=2, lwd=2)
legend("topleft", c("Flow velocity cross map Salinity", "Salinity cross map Flow velocity"), lty=c(1,2), col=c(1,2), lwd=2, bty="n", cex=1.2)

