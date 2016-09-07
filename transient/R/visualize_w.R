inputdata <- read.csv("../csv/result_W_transient.csv", header=FALSE)
N_DATA <- length(inputdata[,1])      #the number of units
TIMESTEP <- length(inputdata[1,])    # the length of X or Y

t <- 1:TIMESTEP

# show  inputdata
W <- array(data = 0, dim = c(N_DATA, TIMESTEP))
W <- inputdata

index <- 3
plot(t, W[index,], type = "l", xlab = "Time step", ylab = "value")

# 画面を 4:1 で分割
layout(matrix(data = c(1, 2), nrow = 1, ncol = 2),
       widths = c(4, 1), heights = c(1, 1))


# カラースケールを作成する
max.value <- max(W)    # 最大値（小数の場合は切り上げて整数にする）
min.value <- min(W)    # 最小値（小数の場合は切り捨てて整数にする）
colorRamp <- rgb(
  seq(1, 1, length=256),   # 赤成分
  seq(1, 0.5, length=256),   # 緑成分
  seq(1, 1, length=256)    # 青成分
)
colorLevels <- seq(min.value, max.value, length = length(colorRamp))

# ヒートマップを描きます
par(mar = c(5.5, 4.5, 2.5, 2))     # 余白調整
image(1:ncol(W), 1:nrow(W), t(W[rev(1:nrow(W)), ]),
      col = colorRamp,
      axes = FALSE,
      main = "Weight W",
      xlab = "genes",
      ylab = "samples",
      zlim = c(min.value, max.value)
)
axis(1, at = 1:ncol(W), labels = colnames(W))
axis(2, at = 1:length(W), labels = colnames(W))
box()                              # ヒートマップの周りの枠線を描く


# カラースケールを描く
par(mar = c(5.5, 2.5, 2.5, 2))
image(1, colorLevels,
      matrix(colorLevels, ncol = length(colorLevels), nrow = 1),
      col = colorRamp, xlab="", ylab="", xaxt="n")
box()
layout(1)
