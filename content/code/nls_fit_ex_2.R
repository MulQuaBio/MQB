# Another NLS Example with climatic scaling data 

# library(ggplot2)
# library(minpack.lm)
library(graphics)

rm(list = ls())  # clear objects
graphics.off()  #close all open figures and graphics objects

############## functions ##############

powMod <- function(x, a, b) {
    return(a * x^b)
}

############## Main code: NLS Fitting ##############
    
MyData <- read.csv("../Data/genome_size.csv")

Data2Fit <- subset(MyData,Suborder == "Anisoptera")

Data2Fit <- Data2Fit[!is.na(Data2Fit$TotalLength),] # remove NA's

plot(Data2Fit$TotalLength, Data2Fit$BodyWeight) # plot data

PowFit <- nls(BodyWeight ~ powMod(TotalLength, a, b), data = Data2Fit, start = list(a = .1, b = .1))

QuaFit <- lm(BodyWeight ~ poly(TotalLength,2), data = Data2Fit)

#Create vector of body lengths for plotting
Lengths <- seq(min(Data2Fit$TotalLength),max(Data2Fit$TotalLength),len=200)

Predic2PlotPow <- powMod(Lengths,coef(PowFit)["a"],coef(PowFit)["b"])

Predic2PlotQua <- predict.lm(QuaFit, data.frame(TotalLength = Lengths))

lines(Lengths, Predic2PlotPow, col = 'blue', lwd = 2.5)
lines(Lengths, Predic2PlotQua, col = 'red', lwd = 2.5)

# Calculate rSS TSS, etc

rSS_Pow <- sum(residuals(PowFit)^2)  # residual sum of squares
TSS_Pow <- sum((Data2Fit$BodyWeight - mean(Data2Fit$BodyWeight))^2)  # Total sum of squares
rSq_Pow <- 1 - (rSS_Pow/TSS_Pow)  # r-squared value

rSS_Qua <- sum(residuals(QuaFit)^2)  # residual sum of squares
TSS_Qua <- sum((Data2Fit$BodyWeight - mean(Data2Fit$BodyWeight))^2)  # Total sum of squares
rSq_Qua <- 1 - (rSS_Qua/TSS_Qua)  # r-squared value

# Now calculate AIC, BIC etc

#Manually
n = nrow(Data2Fit)
kPow = length(coef(PowFit))
kQua = length(coef(QuaFit))

AIC_Pow = n * log((2 * pi) / n) + n + 2 + n * log(rSS_Pow) + 2 * kPow
AIC_Qua = n * log((2 * pi) / n) + n + 2 + n * log(rSS_Qua) + 2 * kQua
AIC_Pow - AIC_Qua

BIC_Pow = n + n * log(2 * pi) + n * log(rSS_Pow / n) + (log(n)) * (kPow + 1)
BIC_Qua = n + n * log(2 * pi) + n * log(rSS_Qua / n) + (log(n)) * (kQua + 1)
BIC_Pow - BIC_Qua

#Automatically
AIC(PowFit) - AIC(QuaFit)
BIC(PowFit) - BIC(QuaFit)
