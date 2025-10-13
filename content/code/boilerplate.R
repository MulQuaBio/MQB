my_function <- function(arg1, arg2) {
  # Statements involving arg1, arg2:
  cat(sprintf("Argument %s is a %s\n", as.character(arg1),
              class(arg1))) # print arg1's type
  cat(sprintf("Argument %s is a %s\n", as.character(arg2),
              class(arg2))) # print arg2's type

  return(c(arg1, arg2)) #this is optional, but very useful
}

my_function(1, 2) #test the function
my_function("Riki", "Tiki") #A different test
