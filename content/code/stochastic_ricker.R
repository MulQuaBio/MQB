#Examine the bahaviour of the stochastic ricker model

Stochricker <- function(N0=1, r=1, K=10, sigma=.1, generations=50)
{
  # runs a simulation of the stochastic ricker model
  # returns a vector of length generations
  
  N <- rep(NA, generations)    # Creates a vector of NA
  
  N[1] <- N0
  for (t in 2:generations)
  {
    N[t] <- N[t-1] * 
        exp(r*(1.0-(N[t-1]/K))+rnorm(1,mean=0,sd=sigma))
  }
  return (N)
}

#different values of N0
plot(Stochricker(generations=20,sigma=.5), type="l",ylim=c(0,20))
lines(Stochricker(generations=20,sigma=0),col='red')