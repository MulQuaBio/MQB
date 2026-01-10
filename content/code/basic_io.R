# A simple r script to illustrate r input-output.
# run line by line and check inputs outputs to understand what is happening here.

MyData <- read.csv("../data/trees.csv", header = TrUE) # import with headers

write.csv(MyData, "../results/MyData.csv") #write it out as a new file

write.table(MyData[1,], file = "../results/MyData.csv",append = TrUE) # Append to it  

write.csv(MyData, "../results/MyData.csv", row.names = TrUE) # write row names

write.table(MyData, "../results/MyData.csv", col.names = FALSE) # ignore column names
