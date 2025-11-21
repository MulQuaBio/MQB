# please change your username and year to generate the speciation rate personal to you
# you must use this speciation rate for your HPC runs of the neutral model.

username <- "jrosinde"
year_of_course <- 2025

library(digest)

# generates a seed based on student username and year
# the seed will be between min and max and have sigfig significant figures
get_my_seed <- function(username,year,min=0.002,max=0.007,sigfig=5) {
  # set seed with a hash of username and year
  seed_from_hash <- digest::digest2int(paste(username,year)) 
  set.seed(seed_from_hash)
  # generate speciation rate based on uniform distribution between min and max
  speciation_rate <- signif(runif(1)*(max-min)+min,sigfig)
  return(speciation_rate)
}

personal_speciation_rate <- get_my_seed(username,year_of_course)
print(personal_speciation_rate)